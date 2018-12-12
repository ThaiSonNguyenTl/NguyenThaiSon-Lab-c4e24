from pymongo import MongoClient
#1 connect database
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
#2 select database
db = client.get_database()
#3 select collection
post_collection = db["posts"]
#4 creat document
new_document1 = {
    "title": "C4E24",
    "post": "khoa hoc lap trinh dau tien cua toi"
}
#5 add document
post_collection.insert_one(new_document1)
#6 close document
client.close()
