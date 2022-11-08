
# Es una función especial en python, retornar una secuencia de valores, pero también suspende la ejecución de la función yield(producir) (no se usa return)

def generador():
    yield 1
    print('Se reanuda la ejecución')
    yield 2
    print('Se reanuda la ejecución')
    yield 3


# Consumir el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))

# consumiendo los valores del generador con un ciclo for
gen = generador()
for valor in gen:
    print(f'Número generado: {valor}')