import mongita
from mongita import MongitaClientDisk
client = MongitaClientDisk()
my_db = client.a_db
pedidos = my_db.pedido

def eliminarPedido(mueble):
    x = pedidos.delete_one(mueble)

def añadirPedido(mueble):
    x = pedidos.insert_one(mueble)

if __name__=="__main__":
    for x in pedidos.find():
        #pedidos.delete_one(x)
        eliminarPedido(x)


