from pymongo import MongoClient

#1ket noi database server

uri ="mongodb://admin:admin123@ds129454.mlab.com:29454/c4e_24"
client = MongoClient(uri)

#2 select database
db = client.get_database()

#3 select collection
post_collection = db["posts"]
for post in post_collection.find(): #coi post_collection la 1 list
    print(post)
# #4 create document
# new_document = {
#     "title": "hom nay vn thang",
#     "post":"Minh  di bao",
# }

# #5 add document into collection them vao collection
# post_collection.insert_one(new_document)

#6 close collection
# client.close()
