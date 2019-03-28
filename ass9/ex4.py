from pymongo import MongoClient

uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
rivers_collection = db["river"]

africa_continent = rivers_collection.find({ "continent": "Africa" })
for each_africa in africa_continent:
    print(each_africa)

print("*" * 120)

america_continent = rivers_collection.find({ "continent": "S. America" })
for each_america in america_continent:
    if(each_america["length"] < 1000 ):
        print(each_america)