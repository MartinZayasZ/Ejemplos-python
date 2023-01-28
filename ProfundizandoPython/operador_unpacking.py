
numeros = [1,2,3]
print(numeros)
print(*numeros, sep=' - ')


def sumar(a,b,c):
    print(f'Resultado de la sema: {a + b +c}')


sumar(*numeros)

# Extraer algunas partes de una lista
mi_lista = [1,2,3,4,5,6]
a, b, c, d, *_ = mi_lista

print(a,b,c,d)

# Unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1, lista2]
lista4 = [*lista1, *lista2]

print('lista de listas', lista3)
print('una sola lista', lista4)

# Unir diccionarios
dic1 = {'a':1, 'b':2, 'c':3}
dic2 = {'d':4, 'e':5}
dic3 = {**dic1, **dic2}
print('Diccionario:', dic3)

# Construir una lista a partir de un str
lista = [*'HolaMundo']
print('Str desempaquetado: ', lista)
print(*lista, sep='')