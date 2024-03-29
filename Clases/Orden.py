from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id = Orden.contador_ordenes
        self._productos = list(productos)

    def addProduct(self, producto):
        self._productos.append(producto)

    def calcularTotal(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        producto_str = ''
        for producto in self._productos:
            producto_str += producto.__str__() + ' | '
        return f'Orden: {self._id},\n Productos: {producto_str}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalon', 300.00)

    productos = [producto1, producto2]

    orden1 = Orden(productos)
    print(orden1)