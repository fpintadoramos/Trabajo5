## Diagrama de la base de datos. 
![image](https://user-images.githubusercontent.com/92045345/152556169-7cd402ec-bae5-45ed-a864-396f189ea445.png) <br/>
### Tablas con las que cuenta 
Esta base de datos cuenta con dos tablas, muebles y pedidos.<br/> 
La tabla muebles almacena los diferentes muebles de los que dispone el almacen.<br/>
La tabla pedidos almacena todos los pedidos que realizamos de los productos.

## Atributos
### Muebles
 1. _id --> Id del producto
 2. nombre --> nombre del producto
 3. precio--> precio del producto
 4. dimensiones --> dimensiones del producto (anchura X altura X longitud)
 5. cant --> cantidad del producto que hay en el almacén
### Pedidos
 1. _id --> Id del pedido
 2. idProducto --> id del producto pedido
 3. cantidad--> cantidad del producto pedido
