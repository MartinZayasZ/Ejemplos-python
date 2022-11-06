
# Los diccionarios guardan un orden a diferencia de un set

diccionario = {
    'Nombre': 'Juan',
    'Apellido': 'Perez',
    'Edad': 28
}
print(diccionario)

# Se agrega una llave con su valor si no se encuentra en el dic
diccionario['Departamento'] = 'Sistemas'
diccionario['Nombre'] = 'Martín'
print(diccionario)

# Recuperar un valor indicando una llave
print(diccionario['Nombre'])
# Método get, recupera una llave y si no existe no lanza Exception
# además podemos regresar un valor en caso de que no exista la llave
print(diccionario.get('Nombre2', 'No sé encontró la llave'))

# setdefault si modifica el diccionario, además de puiede agregar un valor por defaukt
nombre = diccionario.setdefault('Nombres', 'Valor por default')
print(nombre)
print(diccionario)

# Imprimir con pprint
from pprint import pprint as pp
pp(diccionario, sort_dicts=False)