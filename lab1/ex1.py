from pymongo import MongoClient
#1 connect database
uri = "mongodb://admin:admin123@ds129454.mlab.com:29454/c4e_24"
client = MongoClient(uri)
#2 select database
db = client.get_database()
#3 select collection
post_collection = db["posts"]
#4 creat document
account1 = {
    "username":"sonnguyen",
    "email":"thaisonnguyen@gmail.com",
    "phone":"0982121786",
    "password":"18101998",
}
account2 = {
    "username":"admin",
    "email":"thaisonnguyen@gmail.com",
    "phone":"0838623996",
    "password":"18101998",
}
account3 = {
    "username":"admin2",
    "email":"thaisonnguyen@gmail.com",
    "phone":"0838623996",
    "password":"18101998",
}
for post in post_collection.find(): #coi post_collection la 1 list
    print(post)
# post_collection.insert_one(account)
# client.close()
