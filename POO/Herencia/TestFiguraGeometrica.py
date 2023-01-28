from Cuadrado import Cuadrado
from Herencia.FiguraGeometrica import FiguraGeometrica

cuadrado1 = Cuadrado(5, 'rojo')

print(cuadrado1.calcularArea())

# MRO - METHOD RESOLUTION ORDER
print(Cuadrado.mro())

# no se puede instanciar una clase abstracta
# figura = FiguraGeometrica()