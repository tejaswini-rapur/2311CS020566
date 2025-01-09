import pandas as pd

# Step 1: Create a DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}

df = pd.DataFrame(data)

# Step 2: Display the first 2 rows of the DataFrame
print("First 2 rows of the DataFrame:")
print(df.head(2))

# Add a new column named 'Bonus' where the bonus is 10% of the salary
df['Bonus'] = df['Salary'] * 0.10

# Calculate the average salary of employees in the DataFrame
average_salary = df['Salary'].mean()
print("\nAverage Salary of employees:")
print(average_salary)

# Filter and display employees who are older than 25
older_employees = df[df['Age'] > 25]
print("\nEmployees older than 25:")
print(older_employees)