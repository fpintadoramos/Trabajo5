import mongita
from mongita import MongitaClientDisk
client = MongitaClientDisk()
my_db = client.a_db
my_collection = my_db.my_collection


mydict = { "name": "John", "address": "Highway 37", "_id": '61eac8205731c7f26de49a5f'}
x = my_collection.delete_one(mydict)


for x in my_collection.find():
  print(x)