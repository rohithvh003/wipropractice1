import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohithvh@1234",
    database="feb_2026"
)

cursor = conn.cursor()

print("connected to the database successfully")

# INSERT
query1 = "INSERT INTO employee (emid, Empname, Salary) VALUES (105, 'raj', 28000)"
cursor.execute(query1)
conn.commit()

print("Inserted successfully")



# SELECT to print
cursor.execute("select * from employee")
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()
