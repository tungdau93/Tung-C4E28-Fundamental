from pymongo import MongoClient

uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
rivers_collection = db["river"]

continent1_list = rivers_collection.find({ "continent": "Africa" })
for each_continent1 in continent1_list:
    print(each_continent1)

print("*" * 120)

continent2_list = rivers_collection.find({ "continent": "S. America" })
for each_continent2 in continent2_list:
    if(each_continent2["length"] < 1000 ):
        print(each_continent2)