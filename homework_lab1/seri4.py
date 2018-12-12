from matplotlib import pyplot
from pymongo import MongoClient
#1 connect database 
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
#2 select database
db = client.get_database()
#3 select collection
customer_colletion = db["customers"]
# for customer in customer_colletion.find():
amount_event = customer_colletion.count_documents({"ref":"events"})
print(amount_event)
amount_wom = customer_colletion.count_documents({"ref":"wom"})
print(amount_wom)
amount_ads = customer_colletion.count_documents({"ref":"ads"})
print(amount_ads)
# pepare data
ref_count = [amount_event,amount_wom,amount_ads]
#pepare labels
ref_name = ["events","wom","ads"]
#draw pie
pyplot.pie(ref_count,labels=ref_name,autopct="%.1f%%",shadow=True,explode=[0,0.1,0.01])
pyplot.title("events vs wom vs ads")
pyplot.axis("equal")

#show
pyplot.show()