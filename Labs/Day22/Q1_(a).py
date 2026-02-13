import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohithvh@1234",
    database="company_db"
)

cursor = conn.cursor()
print("connected to the database successfully")

print("1. Fetch all employees whose salary is greater than 50,000.")
cursor.execute("SELECT * FROM employees WHERE Salary > 50000")
rows = cursor.fetchall()

for row in rows:
    print(row)
print("2. Insert a new employee record into the table.")

insert_query = "INSERT INTO employees (id, name, department,Salary) VALUES (111, 'Suresh','IT', 60000)"
cursor.execute(insert_query)
conn.commit()

print("3. Update the salary of a specific employee by 10%.")

update_query = "UPDATE employees SET Salary = Salary + (Salary * 0.10) WHERE name = 'Kiran'"
cursor.execute(update_query)
conn.commit()

print("\nSalary updated by 10%")
