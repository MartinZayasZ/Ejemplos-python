class MiClase:

    variable_de_clase = 'Valor1'

    def __init__(self, variable_de_instancia):
        self.variable_de_instancia = variable_de_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_de_clase)

    @classmethod
    def metodoDeClase(cls):
        print(cls.variable_de_clase)

    def metodoInstancia(self):
        self.metodoDeClase()
        self.metodo_estatico()


MiClase.metodoDeClase()
miObjeto1 = MiClase('variable de instancia')
miObjeto1.metodoDeClase()
miObjeto1.metodoInstancia()

# print(MiClase.variable_de_clase)
#
# miClase = MiClase('Valor del objeto')
#
# MiClase.variable_de_clase_2 = 'Valor variable clase 2'
#
# print(miClase.variable_de_instancia)
# print(miClase.variable_de_clase)
#
# print(MiClase.variable_de_clase_2)
