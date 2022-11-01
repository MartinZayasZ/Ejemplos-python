class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad
    def calcularVolumen(self):
        return self.ancho * self.alto * self.profundidad

ancho = float(input(f'Ancho: '))
alto = float(input(f'Alto: '))
profundidad = float(input(f'Profundidad: '))

cubo1 = Cubo(ancho, alto, profundidad)

print(f'El volumen del cubo es: {cubo1.calcularVolumen()}')