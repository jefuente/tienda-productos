#Asignatura: Tienda y Productos
#Objetivos:
#Practica creando clases
#Practicar asociaciones entre clases
#Practica el código de modularización
#Comienza creando una clase de Tienda que tenga 2 atributos: un nombre y una lista de productos. El nombre debe proporcionarse en el momento de la creación, pero la lista de productos debe estar vacía.

#A continuación, crea una clase de Producto que tenga 3 atributos: un nombre, un precio y una categoría. Todo esto debe proporcionarse en el momento de la creación.

#Veamos algunos métodos para nuestra clase de producto:

#update_price(self, percent_change, is_increased) : actualiza el precio del producto. Si is_increased es True, el precio debería aumentar en el porcentaje de cambio proporcionado. Si es False, el precio debe disminuir en el cambio porcentual proporcionado.
#print_info (self) : imprime el nombre del producto, su categoría y su precio.
#También demos algunos métodos a nuestra clase Store:

#add_product (self, new_product) : toma un producto y lo agrega a la tienda
#sell_product (self, id) : elimina el producto de la lista de productos de la tienda dada la identificación (suponga que id es el índice del producto en la lista) e imprima su información.
#inflation(self, percent_increase) : aumenta el precio de cada producto por el percent_increase dado (¡use el método que escribió en la clase Product!)
#set_clearance (self, category, percent_discount) : actualiza todos los productos que coinciden con la categoría dada reduciendo el precio en el percent_discount dado (¡use el método que escribió en la clase Product!)

from clases.producto import Producto
from clases.tienda import Tienda

bebida1 = Producto("Cocacola", 1500, "bebidas", 0)
bebida2 = Producto("Pepsi", 1200,"bebidas",1)
superlider = Tienda("Lider")
superjumbo = Tienda("Jumbo")

superlider.add_product(bebida1)
superlider.add_product(bebida2)
superjumbo.add_product(bebida1)
superjumbo.add_product(bebida2)

superlider.sell_product(0)
superjumbo.sell_product(1)

superlider.inflation(10)