# Luigi


The Python Luigi library is a framework for building complex pipelines of batch jobs.  
It helps users organize their workflows by handling dependencies between tasks in a clear,  
programmatic way. Luigi is particularly useful for tasks like data processing,  
ETL (Extract, Transform, Load) operations, and other batch processing workflows.

Key features of Luigi include:

- **Task Dependency Management:** You can define dependencies between tasks, and Luigi  
  ensures they run in the correct order.
- **Workflow Visualization:** It provides a web interface to monitor workflows, making  
  it easy to debug and visualize your pipelines.
- **Retry and Failure Handling:** It retries failed tasks and provides insights into  
  the reasons for failure.
- **Custom Task Definition:** You can define custom tasks and easily integrate them  
  into your workflows.

If you're working with a lot of data or building pipelines that require complex dependencies,  
Luigi can help simplify and streamline the process.



1. **Workflow**: A workflow is a sequence of tasks or processes designed to achieve a specific goal.
   It outlines how individual tasks are structured, how they depend on each other, and how they
   progress step by step within a system.

2. **Orchestration**: Orchestration involves coordinating and managing multiple workflows or tasks
   to ensure they operate together efficiently. In technology, it often refers to the automation
   of processes, such as managing servers, services, or data pipelines, to work harmoniously.

4. **ETL (Extract, Transform, Load)**: ETL is a process in data integration. 
    - **Extract**: Collect data from multiple sources.
    - **Transform**: Clean, modify, and standardize the data to fit your desired format or requirements.
    - **Load**: Store the processed data into a target system, such as a database or data warehouse.

## Installation

First, install Luigi using pip:

```bash
pip install luigi
```

## Understand Luigi Basics

Luigi operates on the concept of **Tasks**. Each task represents a unit of work, and tasks  
can depend on other tasks. Key components include:

- **requires()**: Defines dependencies (what tasks need to run before this one).
- **output()**: Specifies the output of the task (e.g., a file).
- **run()**: Contains the logic to execute the task.

## Create Your First Luigi Pipeline

Let's build a simple pipeline with two tasks:

1. A task to generate a list of numbers and save it to a file.
2. A task to sum those numbers and save the result.

Create a file called `luigi_intro.py` and add the following code:

```python
import luigi
from luigi import LocalTarget
import json

# Task 1: Generate a list of numbers
class GenerateNumbers(luigi.Task):

    def output(self):
        # Define where the output will be saved
        return LocalTarget("numbers.json")

    def run(self):
        # Generate a list of numbers
        numbers = list(range(1, 11))  # [1, 2, 3, ..., 10]
        
        # Write the numbers to the output file
        with self.output().open("w") as f:
            json.dump(numbers, f)

# Task 2: Sum the numbers
class SumNumbers(luigi.Task):

    def requires(self):
        # This task depends on GenerateNumbers
        return GenerateNumbers()

    def output(self):
        # Define where the sum will be saved
        return LocalTarget("sum.txt")

    def run(self):
        # Read the numbers from the input file
        with self.input().open("r") as f:
            numbers = json.load(f)
        
        # Calculate the sum
        total = sum(numbers)
        
        # Write the result to the output file
        with self.output().open("w") as f:
            f.write(str(total))

# Optional: Run this task directly via command line
if __name__ == "__main__":
    luigi.run()
```

## Run the Pipeline

To execute the pipeline, open your terminal, navigate to the directory containing `luigi_intro.py`, and run:
```bash
python luigi_intro.py SumNumbers --local-scheduler
```

- **`SumNumbers`**: The target task to run.
- **`--local-scheduler`**: Runs Luigi’s built-in scheduler locally (no need for a central server).

Luigi will:
1. Check if `GenerateNumbers` has run (if not, it will run it first).
2. Generate `numbers.json` with `[1, 2, 3, ..., 10]`.
3. Run `SumNumbers` and write `55` (the sum) to `sum.txt`.

#### Step 5: Verify the Output
After running, you’ll see two files:
- `numbers.json`: Contains `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.
- `sum.txt`: Contains `55`.

## How It Works

- **Dependency Management**: `SumNumbers` depends on `GenerateNumbers`. Luigi  
  ensures dependencies are resolved before proceeding.
- **Idempotency**: If you rerun the pipeline and the output files already exist,  
  Luigi skips the tasks unless the files are deleted or modified.  
- **Output Tracking**: The `LocalTarget` class represents files on your local filesystem,
   but Luigi supports other targets like S3, HDFS, etc.

## Extend the Pipeline

Let’s add a third task to calculate the average. Update `luigi_intro.py`:

```python
import luigi
from luigi import LocalTarget
import json

class GenerateNumbers(luigi.Task):
    def output(self):
        return LocalTarget("numbers.json")

    def run(self):
        numbers = list(range(1, 11))
        with self.output().open("w") as f:
            json.dump(numbers, f)

class SumNumbers(luigi.Task):
    def requires(self):
        return GenerateNumbers()

    def output(self):
        return LocalTarget("sum.txt")

    def run(self):
        with self.input().open("r") as f:
            numbers = json.load(f)
        total = sum(numbers)
        with self.output().open("w") as f:
            f.write(str(total))

# New Task: Calculate the average
class AverageNumbers(luigi.Task):
    def requires(self):
        return SumNumbers()

    def output(self):
        return LocalTarget("average.txt")

    def run(self):
        with self.input().open("r") as f:
            total = float(f.read())
        with self.requires().input().open("r") as f:
            numbers = json.load(f)
        average = total / len(numbers)
        with self.output().open("w") as f:
            f.write(str(average))

if __name__ == "__main__":
    luigi.run()
```

Run it with:

```bash
python luigi_intro.py AverageNumbers --local-scheduler
```

Now, `average.txt` will contain `5.5`.

#### Step 7: Explore Advanced Features
- **Parameters**: Add `luigi.Parameter()` to make tasks configurable (e.g., change the range of numbers).
- **Central Scheduler**: Run `luigid` in a separate terminal for a web-based UI (`pip install luigi[tornado]` required).
- **External Targets**: Use `luigi.contrib` modules for databases, cloud storage, etc.


For more details, check the [official Luigi documentation](https://luigi.readthedocs.io/).
