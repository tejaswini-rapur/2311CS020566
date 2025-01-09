import pandas as pd

# 1. Create the DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}

df = pd.DataFrame(data)

# 2. Display the first 2 rows
first_two_rows = df.head(2)

# 3. Add a new column for Bonus (10% of the salary)
df['Bonus'] = df['Salary'] * 0.10

# 4. Calculate the average salary
average_salary = df['Salary'].mean()

# 5. Filter and display employees older than 25
older_than_25 = df[df['Age'] > 25]

(first_two_rows, df, average_salary, older_than_25)
