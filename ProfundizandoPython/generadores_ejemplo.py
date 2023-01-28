
#generador de números, 1 al 5
def generador_numeros():
    for numero in range(1, 6):
        yield numero
        print('Se reanuda la ejeción de la función')

# utilizamos el generador
generador = generador_numeros()

print(f'Objeto generado: {generador}')
print(type(generador))

# consumimos los valores del generador
for valor in generador:
    print(f'Número generado: {valor}')

generador = generador_numeros()
try:
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
except StopIteration as e:
    print(f'Error al consumir generador: {e}')

# OtRA FORMA DE CONSUMIR UN GENERADOR
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f'Impresión del valor generado: {valor}')
    except StopIteration as e:
        print('Se terminó de iterar el generador')
        break