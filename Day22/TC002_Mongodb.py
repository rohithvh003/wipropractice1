from pymongo import MongoClient

# connection
client = MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB")

# database
db = client["feb_2026"]

# collection
collection = db["Company"]

# insert
employee = {
    "name": "Rohith",
    "age": 25,
    "salary": 75000
}

result = collection.insert_one(employee)
print("Inserted ID:", result.inserted_id)

# display all
print("\nAll documents in collection:")
for doc in collection.find():
    print(doc)
