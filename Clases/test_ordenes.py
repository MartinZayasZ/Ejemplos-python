from Orden import Orden
from Producto import Producto

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 300.00)
producto3 = Producto('Calcetin', 25.00)
producto4 = Producto('Blusa', 80.00)

productos = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos)
orden1.addProduct(producto3)
orden1.addProduct(producto4)
print(orden1)
print(orden1.calcularTotal())

orden2 = Orden(productos2)
print(orden2)
print(orden2.calcularTotal())