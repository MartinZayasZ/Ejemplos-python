class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        # Ordenamos siempre los elementos
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        self.ordenar()

class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        super().__init__(elementos)
    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')
    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)

class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass

class OtraClase():
    pass



lista_simple = ListaSimple([5,3,6,8,])
print(lista_simple)

lista_ordenada = ListaOrdenada([5,3,6,8,-10])
lista_ordenada.agregar(-7)
print(lista_ordenada)

lista_enteros = ListaEnteros([-10,1,2,4,6,7,9,8,10,11])
lista_enteros.agregar(10)
print(lista_enteros)

lista_enteros_ordenada = ListaEnterosOrdenada([4,4,10,14,-14])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(lista_enteros_ordenada)

# saber las clases padre y su orden
print(ListaEnterosOrdenada.__bases__)
# MRO (Method resolution order)
print(ListaEnterosOrdenada.__mro__)


#isintance
print(f'Es entero? {isinstance("10", int)}')
print('Es cadena?', isinstance('hola', str))
print('Es lista enteros ordenada?', isinstance(lista_enteros_ordenada, ListaEnterosOrdenada))
print('Es lista de enteros?', isinstance(lista_enteros_ordenada, ListaEnteros))
print('Es otra clase?', isinstance(lista_enteros_ordenada, OtraClase))
