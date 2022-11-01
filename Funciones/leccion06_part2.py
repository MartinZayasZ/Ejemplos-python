def sumar(a:int = 0, b:int = 0) -> int:
    return a + b

resultado = sumar(5)
print(f'Resultado de la suma: {resultado}')


def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Martin', 'Sergio', 'Iván')
listarNombres('Laura', 'Carlos')


def sumarVariable(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(f'Total: {sumarVariable(5, 7, 10, 14)}')