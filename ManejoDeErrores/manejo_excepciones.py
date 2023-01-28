from NumerosIdenticosException import NumerosIdenticosException

resultado = None


try:

    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        raise NumerosIdenticosException('Números identicos')

    resultado = a / b
except ZeroDivisionError as e:
    print(f'Error: {e}')
except TypeError as e:
    print(f'Type error: {e}')
except TimeoutError as e:
    print(f'Error: {e}')
except Exception as e:
    print(f'Generic Error: {e}')
else:
    print('No se arrojó ninguna execpción')
finally:
    print(f'Ejecución de bloque finally')


print(f'Resultado: {resultado}')