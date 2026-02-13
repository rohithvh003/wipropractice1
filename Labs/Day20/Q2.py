import pandas as pd

data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)
print(df)

print("IT Employees")

IT_Employee = df[df["Department"] == "IT"]
print(IT_Employee)

avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

print("Salary increased by 10%")
df["Salary_Adjusted"] = df["Salary"] * 1.10
print(df)