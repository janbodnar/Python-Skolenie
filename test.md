# Code samples


```python
import faker
import csv

faker = faker.Faker()

n = 100_000

fname = "users.csv"

with open(fname, 'w') as f:

    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['First name', 'Last name', 'Salary'])

    for _ in range(n):

        fname = faker.first_name()
        lname = faker.last_name()
        salary = faker.random_int(850, 3000, 50)

        writer.writerow([fname, lname, salary])
```
