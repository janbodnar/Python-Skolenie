# Processing Bookstore XML Data

## Prerequisites

Install required dependencies:
  
```bash
pip install luigi pandas requests
```

## Define the Modified Pipeline

Create a file called `luigi_bookstore.py` with the following code:

```python
import luigi
from luigi import LocalTarget, Parameter
import pandas as pd
import requests
import json
from datetime import datetime
import xml.etree.ElementTree as ET

# Task 1: Download XML data from webcode.me
class DownloadData(luigi.Task):
    url = Parameter(default="http://webcode.me/bookstore.xml")

    def output(self):
        return LocalTarget("bookstore_raw.xml")

    def run(self):
        # Download the XML file
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an error if the request fails
        
        # Save the raw XML to a file
        with self.output().open("w") as f:
            f.write(response.text)

# Task 2: Clean and convert XML to CSV
class CleanData(luigi.Task):
    url = Parameter(default="http://webcode.me/bookstore.xml")

    def requires(self):
        return DownloadData(url=self.url)

    def output(self):
        return LocalTarget("bookstore_cleaned.csv")

    def run(self):
        # Parse the XML file
        tree = ET.parse(self.input().path)
        root = tree.getroot()
        
        # Extract book data into a list of dictionaries
        books = []
        for book in root.findall("book"):
            book_data = {
                "id": book.get("id"),
                "author": book.find("author").text,
                "title": book.find("title").text,
                "genre": book.find("genre").text,
                "price": float(book.find("price").text),
                "publish_date": book.find("publish_date").text,
                "description": book.find("description").text.strip()
            }
            books.append(book_data)
        
        # Convert to DataFrame and clean
        df = pd.DataFrame(books)
        # Example cleaning: Remove books with price <= 0 (none in this dataset, but as a precaution)
        df = df[df["price"] > 0].copy()
        # Add a processed timestamp
        df["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save to CSV
        df.to_csv(self.output().path, index=False)

# Task 3: Analyze the cleaned data
class AnalyzeData(luigi.Task):
    url = Parameter(default="http://webcode.me/bookstore.xml")

    def requires(self):
        return CleanData(url=self.url)

    def output(self):
        return LocalTarget("bookstore_analysis.json")

    def run(self):
        # Read cleaned data
        df = pd.read_csv(self.input().path)
        
        # Calculate statistics
        stats = {
            "total_books": len(df),
            "average_price": df["price"].mean(),
            "genre_counts": df["genre"].value_counts().to_dict(),
            "most_expensive_book": {
                "title": df.loc[df["price"].idxmax(), "title"],
                "price": df["price"].max()
            },
            "oldest_book": {
                "title": df.loc[df["publish_date"].idxmin(), "title"],
                "publish_date": df["publish_date"].min()
            }
        }
        
        # Save results as JSON
        with self.output().open("w") as f:
            json.dump(stats, f, indent=4)

# Task 4: Generate a report
class GenerateReport(luigi.Task):
    url = Parameter(default="http://webcode.me/bookstore.xml")
    report_format = Parameter(default="txt")  # txt or json

    def requires(self):
        return {
            "raw": DownloadData(url=self.url),
            "analysis": AnalyzeData(url=self.url)
        }

    def output(self):
        return LocalTarget(f"bookstore_report.{self.report_format}")

    def run(self):
        # Load analysis
        with self.input()["analysis"].open("r") as f:
            analysis = json.load(f)
        
        # Generate report content
        report_content = (
            f"Bookstore Data Report\n"
            f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"Total Books: {analysis['total_books']}\n"
            f"Average Price: ${analysis['average_price']:.2f}\n"
            f"Most Expensive Book: {analysis['most_expensive_book']['title']} (${analysis['most_expensive_book']['price']})\n"
            f"Oldest Book: {analysis['oldest_book']['title']} ({analysis['oldest_book']['publish_date']})\n"
            f"Genre Distribution: {analysis['genre_counts']}\n"
        )
        
        # Write report based on format
        with self.output().open("w") as f:
            if self.report_format == "txt":
                f.write(report_content)
            elif self.report_format == "json":
                json.dump({"report": report_content.split("\n")}, f, indent=4)

# Run the pipeline
if __name__ == "__main__":
    luigi.run()
```

#### Step 2: Run the Pipeline
Run the pipeline with these commands:

1. **Default run (txt report)**:
   ```bash
   python luigi_bookstore.py GenerateReport --local-scheduler
   ```

2. **JSON report format**:
   
 ```bash
 python luigi_bookstore.py GenerateReport --report-format json --local-scheduler
 ```

4. **Custom URL (though we’ll stick with the default here)**:
   
 ```bash
 python luigi_bookstore.py GenerateReport --url "http://webcode.me/bookstore.xml" --local-scheduler
 ```

## Tasks

- **DownloadData**: Fetches the XML from `http://webcode.me/bookstore.xml` and saves it as `bookstore_raw.xml`.
- **CleanData**: Parses the XML, converts it to a CSV (`bookstore_cleaned.csv`), and adds a `processed_at` column.
- **AnalyzeData**: Analyzes the data (e.g., average price, genre counts) and saves results to `bookstore_analysis.json`.
- **GenerateReport**: Creates a summary report in the specified format (`bookstore_report.txt` or `bookstore_report.json`).

## Verify the Output

After running, check these files:
- `bookstore_raw.xml`: The original XML data.
- `bookstore_cleaned.csv`: A table with columns `id`, `author`, `title`, `genre`, `price`, `publish_date`, `description`, and `processed_at`.
- `bookstore_analysis.json`: Statistics about the books.
- `bookstore_report.txt` or `bookstore_report.json`: A human-readable summary.

For `report_format=json`, `bookstore_report.json` would contain the same info in structured form.

