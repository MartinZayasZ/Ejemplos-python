# Orden de inicialización de objetos

class Padre:
    def __init__(self):
        print('Inicializador Padre')

    def metodo(self):
        print('método padre')

class Hijo(Padre):
    # se manda a llamar el método INIT de la clase padre, siempre y cuando la hija no defina su propio método INIT

    def __init__(self):
        # de manera opcional, podemos llamar el método init de la clase padre (super)
        super().__init__()
        print('Inicializador hijo')
    def metodo(self):
        super().metodo()
        print('método hijo')

# padre1 = Padre()
# padre1.metodo()

hijo1 = Hijo()
hijo1.metodo()
