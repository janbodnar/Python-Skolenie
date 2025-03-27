## User Data Pipeline

Luigi is a Python library for building and managing data pipelines, ideal for orchestrating  
tasks with dependencies. In this tutorial, we’ll create a pipeline that generates fake user data,   
processes it, and produces multiple outputs. This example introduces Luigi’s core concepts like tasks, 
dependencies, and outputs in a practical way.

#### Prerequisites

- Python 3.x installed
- Basic Python knowledge
- Install dependencies:
- 
  ```bash
  pip install luigi faker pandas openpyxl
  ```

## Install Luigi

Ensure Luigi is installed:
```bash
pip install luigi
```

## Understand Luigi Basics

Luigi uses **Tasks** to define workflow steps:

- **`requires()`**: Specifies dependencies (tasks that must complete first).
- **`output()`**: Defines the task’s output (e.g., a file).
- **`run()`**: Contains the task’s execution logic.

## Create the User Data Pipeline

We’ll build a pipeline with six tasks:

1. Generate 100 fake users with some missing `email` or `last_name` fields and zip them.
2. Unzip the data.
3. Clean the data by removing users without `email` or `last_name`.
4. Export the cleaned data to an Excel file.
5. Export the cleaned data to an SQLite database.
6. Generate a report summarizing the process.

Create a file called `luigi_user_intro.py` with this code:

```python
import luigi
from luigi import LocalTarget, Parameter
from faker import Faker
import pandas as pd
import json
import random
import zipfile
import os
from datetime import datetime
import sqlite3

# Initialize Faker
fake = Faker()

# Task 1: Generate and zip user data
class GenerateUsers(luigi.Task):
    def output(self):
        return LocalTarget("users_raw.zip")

    def run(self):
        # Generate 100 users with some missing email/last_name
        users = []
        for i in range(100):
            user = {
                "id": i + 1,
                "first_name": fake.first_name(),
                "last_name": "" if random.random() < 0.1 else fake.last_name(),  # 10% chance of missing last_name
                "email": "" if random.random() < 0.15 else fake.email(),        # 15% chance of missing email
                "city": fake.city(),
                "salary": round(random.uniform(30000, 120000), 2)
            }
            users.append(user)
        
        # Save to a temporary CSV
        temp_csv = "users_raw.csv"
        df = pd.DataFrame(users)
        df.to_csv(temp_csv, index=False)
        
        # Zip the CSV
        with zipfile.ZipFile(self.output().path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            zf.write(temp_csv, arcname="users_raw.csv")
        
        # Clean up
        os.remove(temp_csv)

# Task 2: Unzip the data
class UnzipData(luigi.Task):
    def requires(self):
        return GenerateUsers()

    def output(self):
        return LocalTarget("users_extracted.csv")

    def run(self):
        # Unzip the archive
        with zipfile.ZipFile(self.input().path, "r") as zf:
            zf.extract("users_raw.csv", path=".")
        
        # Move extracted file
        os.rename("users_raw.csv", self.output().path)

# Task 3: Clean the data
class CleanData(luigi.Task):
    def requires(self):
        return UnzipData()

    def output(self):
        return LocalTarget("users_cleaned.csv")

    def run(self):
        # Read the extracted data
        df = pd.read_csv(self.input().path)
        
        # Clean: Remove rows with missing email or last_name
        df_cleaned = df[
            (df["email"].notna() & (df["email"].str.strip() != "")) &
            (df["last_name"].notna() & (df["last_name"].str.strip() != ""))
        ].copy()
        df_cleaned["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save cleaned data
        df_cleaned.to_csv(self.output().path, index=False)

# Task 4: Export to Excel
class ExportToExcel(luigi.Task):
    def requires(self):
        return CleanData()

    def output(self):
        return LocalTarget("users_cleaned.xlsx")

    def run(self):
        # Read and export to Excel
        df = pd.read_csv(self.input().path)
        df.to_excel(self.output().path, index=False)

# Task 5: Export to SQLite
class ExportToSQLite(luigi.Task):
    def requires(self):
        return CleanData()

    def output(self):
        return LocalTarget("users.db")

    def run(self):
        # Read and export to SQLite
        df = pd.read_csv(self.input().path)
        conn = sqlite3.connect(self.output().path)
        df.to_sql("users", conn, if_exists="replace", index=False)
        conn.close()

# Task 6: Generate a report
class GenerateReport(luigi.Task):
    report_format = Parameter(default="txt")  # txt or json

    def requires(self):
        return {"raw": UnzipData(), "cleaned": CleanData()}

    def output(self):
        return LocalTarget(f"users_report.{self.report_format}")

    def run(self):
        # Load raw and cleaned data
        raw_df = pd.read_csv(self.input()["raw"].path)
        cleaned_df = pd.read_csv(self.input()["cleaned"].path)
        
        # Calculate stats
        stats = {
            "total_raw_users": len(raw_df),
            "total_cleaned_users": len(cleaned_df),
            "removed_users": len(raw_df) - len(cleaned_df),
            "average_salary": cleaned_df["salary"].mean(),
            "top_cities": cleaned_df["city"].value_counts().head(3).to_dict()
        }
        
        # Generate report content
        report_content = (
            f"User Data Processing Report\n"
            f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"Total Raw Users: {stats['total_raw_users']}\n"
            f"Total Cleaned Users: {stats['total_cleaned_users']}\n"
            f"Users Removed: {stats['removed_users']}\n"
            f"Average Salary: ${stats['average_salary']:.2f}\n"
            f"Top 3 Cities: {stats['top_cities']}\n"
        )
        
        # Write report
        with self.output().open("w") as f:
            if self.report_format == "txt":
                f.write(report_content)
            elif self.report_format == "json":
                json.dump({"report": report_content.split("\n")}, f, indent=4)

if __name__ == "__main__":
    luigi.run()
```

## Run the Pipeline

Navigate to the directory with `luigi_user_intro.py` and run:

```bash
python luigi_user_intro.py GenerateReport --local-scheduler
```

For a JSON report:

```bash
python luigi_user_intro.py GenerateReport --report-format json --local-scheduler
```

## Verify the Output

After running, you’ll see:

- `users_raw.zip`: Zipped raw CSV with 100 users.
- `users_extracted.csv`: Unzipped raw data.
- `users_cleaned.csv`: Cleaned data (no missing `email` or `last_name`).
- `users_cleaned.xlsx`: Excel file with cleaned data.
- `users.db`: SQLite database with a `users` table.
- `users_report.txt` (or `.json`): Summary report.

**Example Report (txt):**
```
User Data Processing Report
Generated on: 2025-03-27 17:00:00

Total Raw Users: 100
Total Cleaned Users: 78
Users Removed: 22
Average Salary: $75123.45
Top 3 Cities: {'New York': 4, 'Chicago': 3, 'Seattle': 3}
```

## How It Works

- **Dependency Management**: Each task depends on the previous one (e.g., `CleanData` requires `UnzipData`), ensuring proper execution order.
- **Data Cleaning**: The `CleanData` task uses robust filtering to remove invalid users.
- **Multiple Outputs**: The pipeline produces files in different formats (CSV, Excel, SQLite, text/JSON).
- **Idempotency**: Luigi skips tasks if their outputs already exist, unless the files are deleted.

## Extend the Pipeline

Try these enhancements:
- Add a `num_users` parameter to `GenerateUsers` to customize the number of users.
- Include a task to validate emails with a regex.
- Use `matplotlib` to generate a salary distribution chart.

## Conclusion

This pipeline demonstrates Luigi’s power in managing a multi-step workflow with real-world  
data processing. It’s a great starting point for learning how to structure tasks and handle   
dependencies. 

