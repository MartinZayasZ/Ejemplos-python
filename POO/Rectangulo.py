class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcularArea(self):
        return self.base * self.altura


base = float(input('Base: '))
altura = float(input('Altura: '))

rectangulo1 = Rectangulo(base, altura)

print(f'El area es de: {rectangulo1.calcularArea()}')