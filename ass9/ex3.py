from pymongo import MongoClient
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
customers_collection = db["customers"]

ref_events = customers_collection.find({ "ref": "events" })
count_events = len(list(ref_events))
print("Count the number of customers group by events:", count_events)
ref_wom = customers_collection.find({ "ref": "wom" })
count_wom = len(list(ref_wom))
print("Count the number of customers group by wom:", count_wom)
ref_ads = customers_collection.find({ "ref": "ads" })
count_ads = len(list(ref_ads))
print("Count the number of customers group by ads:", count_ads)

count_list = [count_events, count_wom, count_ads]
print(count_list)
name_list = ["Events", "Wom", "Ads"]

pyplot.pie(count_list, labels = name_list, autopct = "%.1f%%", shadow = True, explode = [0.02, 0.02, 0.02])
pyplot.title("Events, Wom and Ads percentage of reference")
pyplot.show()
