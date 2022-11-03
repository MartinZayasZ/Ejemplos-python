
nombres1 = ['Martin', 'Teresita', 'Manuel']
nombres2 = 'Laura María Gonzalo Ernesto'.split()

# Sumar listas
print(f'Sumar listas: {nombres1+nombres2}')

# Extender lista con otra lista
nombres1.extend(nombres2)
print(f'Extender la lista 1: {nombres1}')

# Lista de números
numeros1 = [10, 40, 15, 4, 20, 90, 4]
print(f'Lista original: {numeros1}')
# obtener el índice del primer elemento encontrado
# help(list.index)
print(f'índice 4: {numeros1.index(4)}')

# Invertir el orden de los elemento de una lista
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

# Ordenas los elementos de una lista
numeros1.sort()
print(f'Lista ordenada: {numeros1}')
# Ordenas de manera descendente una lista
numeros1.sort(reverse=True)
print(f'Lista descendente: {numeros1}')

# Obtener el valor min y max de una lista
print(f'Valor mínimo: {min(numeros1)}')
print(f'Valor máximo: {max(numeros1)}')

# Copiar los elementos de una lista
numeros2 = numeros1.copy()
# podemos usar el constructor de la lista
# numeros2 = list(numeros1)
print(numeros1, numeros2)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')


# slicing
numeros2 = numeros1[:]
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

# Multiplicación de listas
lista_multiplicacion = 5*[[2,5]]
print(lista_multiplicacion)
print(f'Misma referencia? {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Mismo contenido? {lista_multiplicacion[0] == lista_multiplicacion[1]}')

lista_multiplicacion[2].append(10)
print(lista_multiplicacion)

# Matrices
matriz = [[10,20], [30,40,50], [60,70,80]]
print(f'Matriz original: {matriz}')


lista_listas = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
lista_listas.sort(key=len)
print(f'Ordenar lista: {lista_listas}')

# sorted built-in
# help(sorted)
nombres1 = ['Juan', 'Carlos', 'Karla', 'Pedro']
nombres1 = sorted(nombres1)
print(f'Sorted: {nombres1}')
nombres1 = sorted(nombres1, reverse=True)
print(f'Sorted: {nombres1}')

nombres1 = sorted(nombres1, key=len)
print(f'Sorted len: {nombres1}')