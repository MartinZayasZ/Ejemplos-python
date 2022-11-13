class Clase1:
    def __init__(self):
        print('Clase1.__init__')
    def metodo(self):
        print('Método Clase1')

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()
    def metodo(self):
        print('Método Clase2')
        super().metodo()

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()
    def metodo(self):
        print('Método Clase3')
        super().metodo()

class Clase4(Clase2, Clase3):
    pass
    def metodo(self):
        print('Método Clase4')
        super().metodo()


# Creamos un objeto de la clase 4
clase4 = Clase4()
print(Clase4.__bases__)
print(Clase4.__mro__)

# cuál método se ejecuta?
clase4.metodo()