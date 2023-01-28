# Permiten transformar de manera prorgamatica nuestra clase
# es similar a los decoradres de funciones (meta programación)
import inspect


def decorador_rpr(cls):
    print('Se ejecuto decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # Revisamos los atributos de la clase con el método vars
    atributos = vars(cls)
    #for nombre, atributo in atributos.items():
    #    print(nombre, atributo)

    # Revisamos si se ha sobreescrito el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método init')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma método init: {firma_init}')

    # Recuperamos los parámetros excepto self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parámetros __init__: {parametros_init}')

    # Revisamos si cada parámetro tiene un método property asociado
    for parametro in parametros_init:
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un método property para el parametro: {parametro}')

    # Creamos el método repr dinámicamente
    def metodo_repr(self):
        # Expresión generadora
        generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        # Lista del generador
        lista_arg = list(generador_arg)
        print(f'Lista del generador: {lista_arg}')
        # creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del método repr: {argumentos}')
        return f'{cls.__name__}({argumentos})'

    # Agregar dinámicamente el método repr a nuestra clase
    setattr(cls, '__repr__', metodo_repr)

    return cls

@decorador_rpr
class Persona:
    def __init__(self, nombre, apellido):
        print('se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

#    def __repr__(self):
#        return f'Persona({self._nombre}, {self._apellido})'

persona1 = Persona('Juan', 'Perez')
print(persona1)

# tiene los métodos de propiedad nombre, apellido, repr
print(dir(persona1))
# tiene el método repr sobreescrito?
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)