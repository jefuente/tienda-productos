
class Producto:
    def __init__(self, nombre, precio, categoria, codigo):
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria
        self.codigo=codigo
    def update_price(self, percent_change, is_increased=True):
        if is_increased:
            self.precio +=self.precio*percent_change/100
        else:
            self.precio -=self.precio*percent_change/100
        return self
    def print_info (self):
        print(f"El nombre del producto es {self.nombre}, pertenece a la categoria {self.categoria} y su precio es de ${self.precio}")
        return self
