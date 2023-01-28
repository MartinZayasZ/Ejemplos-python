class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f'Vehículo: {self.color} {self.ruedas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return f'{super().__str__()} Velocidad: {self.velocidad}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return f'{super().__str__()} Tipo: {self.tipo}'



vehiculo1 = Vehiculo('rojo', 4)
print(vehiculo1)

coche1 = Coche('guinda', 4, 100)
print(coche1)

bicicleta1 = Bicicleta('azul', 2, 'BMX')
print(bicicleta1)