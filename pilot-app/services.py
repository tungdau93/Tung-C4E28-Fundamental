from pymongo import MongoClient
from faker import Faker
from random import randint, choice
from bson.objectid import ObjectId

faker = Faker()

uri = "mongodb+srv://admin:admin@c4e28-jxucw.mongodb.net/test?retryWrites=true"
# 1. Connect cluster
client = MongoClient(uri)

# 2. Get/create database 
service_database = client.db_service

# 3. Create collections
service_collection = service_database["services"]
# 4. Create/insert document
# for i in range(50):
#     new_service = {
#         "name": faker.name(),
#         "age": randint(18, 30),
#         "address": faker.address(),
#         "gender": choice(["male", "female"]),
#         "available": choice([True, False])
#     }
#     service_collection.insert_one(new_service)
#     print("Saving document {0} ...".format(i+1))

# 5. Read
# 5.1 Read all
# all_services = service_collection.find() # cơ chế lazy loading
# all_services được coi như là 1 list
# for service in all_services:
#     print(service)
# 5.2 Read one
# one_service = service_collection.find_one({ "name": "Charles Chung" })
# chỉ trả về cho mình duy nhất 1 document
# print(one_service["gender"])
# one_service = service_collection.find_one({ "_id": ObjectId("5c9a1d679f78393f742831f3") })
# print(one_service)

# 6. Delete
# service = service_collection.find_one({ "name": "Anthony Scott" })
# if service is not None:
#     service_collection.delete_one(service)
# else:
#     print("not found document!")

# 7. Update
# one_service = service_collection.find_one({ "_id": ObjectId("5c9a1d6b9f78393f742831fe") })
# new_value = { "$set": { "gender": "male" } }
# service_collection.update_one(one_service, new_value)
