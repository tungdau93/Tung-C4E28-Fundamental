import mongodb

database = mongodb.connect()
services = database["posts"]
