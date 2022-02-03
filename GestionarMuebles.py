import mongita
from mongita import MongitaClientDisk
client = MongitaClientDisk()
my_db = client.a_db
my_collection = my_db.my_collection

def eliminarMueble(mueble):
    x = my_collection.delete_one(mueble)

def añadirMueble(mueble):
    x = my_collection.insert_one(mueble)

if __name__=="__main__":
    for x in my_collection.find():
        my_collection.delete_one(x)


