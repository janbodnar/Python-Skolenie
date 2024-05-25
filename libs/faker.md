# Faker 


## Names

```python
from faker import Faker

faker = Faker()

print(f'Name: {faker.name()}')
print(f'First name: {faker.first_name()}')
print(f'Last name: {faker.last_name()}')

print('--------------------------')

print(f'Male name: {faker.name_male()}')
print(f'Female name: {faker.name_female()}')
```

## Jobs

```python
from faker import Faker

faker = Faker()

for _ in range(6):
    print(faker.job())
```
