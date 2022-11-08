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