def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

resultado = factorial(4)
print(f'El factorial de 5 es: {resultado}')

def imprimir_numeros(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros(numero - 1)

imprimir_numeros(10)