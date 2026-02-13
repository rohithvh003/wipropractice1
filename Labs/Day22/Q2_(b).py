
from pymongo import MongoClient

# connection
client = MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB")

# database
db = client["company_db"]

# collection
collection = db["employee"]

# insert
employee = {
    "name": "Rohith",
    "department": "IT",
    "salary": 75000
}
collection.insert_one(employee)
print("Employee inserted")


# find IT department
print("\nEmployees in IT department:")
for doc in collection.find({"department": "IT"}):
    print(doc)


collection.update_one(
    {"name": "Rohith"},
    {"$set": {"salary": 70000}}
)

print("\nSalary updated")

# verify update
print("\nAfter update:")
print(collection.find_one({"name": "Rohith"}))
