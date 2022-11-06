
# print(dir(__builtins__))

# help(zip)


numeros = [1,2,3]
letras = ['a', 'b', 'c']
identificadores = 321,322,323,324,325
conjunto = {6,4,0,9,8,15,101}
mezcla = zip(numeros,letras,identificadores,conjunto)

# print('Mezcla', mezcla)
print(list(mezcla))
# print(tuple(zip(numeros, letras)))
#
# print(type(mezcla))

# Iterar en paralelo
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    print(f'Número: {numero}, Letra: {letra}, Id: {id}, Aleatorio: {aleatorio}')

nueva_lista = []

for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nueva_lista)

# unzip
mezcla = [(1,'a'),(2,'b'),(3,'c')]
numeros, letras = zip(*mezcla)

print(f'Números: {numeros}, Letras: {letras}')

# Ordenamiento
letras = ['c', 'd', 'a', 'e', 'b']
numeros = [3, 2, 4, 1, 0]
mezcla = zip(letras, numeros)
# sin orden
print(tuple(mezcla))
# ordenar por letra(primer iterable)
print(sorted(zip(letras, numeros)))
# ordenar por número
print(sorted(zip(numeros, letras)))

# diccionario con zip y dos iterables
llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 18]
diccionario = dict(zip(llaves, valores))
print(f'Diccionario: {diccionario}')

# Actualizar un elemento de un diccionario
llave = ['Edad']
nueva_edad = [27]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)

