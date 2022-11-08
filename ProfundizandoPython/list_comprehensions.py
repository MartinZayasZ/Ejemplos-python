numeros = range(10)
lista_pares = []

# creamos una nueva lista, con los valores pares, multiplicado por si mismo
for numero in numeros:
    # revisamos si es un número par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print('Lista pares:', lista_pares)

# hacemo lo mismo pero con list comprehensions
# [expresion for var in coleccion if condicion]
# la condición del if es opcional
#lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero % 2 == 0]
print(f'Lista pares: {lista_pares}')

# ejemplo similar con dos concidiciones, opcionales
lista_pares = [numero for numero in range(50) if numero % 2 == 0 if numero % 6 == 0 ]
print(f'Lista pares y divisible entre 6: {lista_pares}')

# agregando if else
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Lista pares: {lista_pares}')
print(f'Lista impares: {lista_impares}')

# el mismo ejercicio usando lista comprehensions
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero%2==0 else lista_impares.append(numero) for numero in range(10)]
print(f'Lista pares: {lista_pares}')
print(f'Lista impares: {lista_impares}')

# Lista de listas
lista_listas = [[1,2,3], [4,5,6], [7,8,9,10]]
# convertimos la lista de listas en una sola lista
lista_simple = [valor for sublista in lista_listas for valor in sublista]
print(f'Lista simple: {lista_simple}')

# ahora creamos una lista de numeros pares a partir de la lisda de listas
# sin list comprehensions
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor % 2 == 0:
            lista_pares.append(valor)
print(f'Lista pares sin list comprehensions: {lista_pares}')

lista_pares = [valor for sublista in lista_listas for valor in sublista if valor%2==0]
print(f'Lista pares con list comprehensions: {lista_pares}')

