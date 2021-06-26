class Tienda:
    def __init__(self, nombre):
        self.nombre=nombre
        self.productos=[]
    def add_product(self, new_product):
        self.productos.append(new_product)
        print(f"Se ha incorporado el producto a la tienda")
        return self
    def sell_product(self, codigo):
        id = -1
        for producto in self.productos:
            id+=1
            if producto.codigo == codigo:
                break
        producto = self.productos.pop(id)
        producto.print_info()
        print(f"El producto {producto.nombre} con codigo {codigo} fue eliminado.")

    def inflation(self, percent_increase):
        for producto in self.productos:
            producto.update_price(percent_increase,True)
    def set_clearance (self, category, percent_discount):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.update_price(porcentaje,False)

