
def calculadora(a, b, operacion = 'sumar'):
    # Función anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    # Llamamos a la función anidada
    if operacion == 'sumar':
        print(f'Suma: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resta: {restar(a, b)}')

calculadora(5,6, 'sumar')
calculadora(5,6, 'restar')
