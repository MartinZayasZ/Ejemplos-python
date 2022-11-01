class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'Id producto: {self._id}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 300.00)
    print(producto2)