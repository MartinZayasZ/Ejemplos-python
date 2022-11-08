# Expresión generadora (es un generador anónimo)

multiplicacion = (valor*valor for valor in range(4))


for resultado in multiplicacion:
    print(f'Resultado: {resultado}')

# también se puede pasar una expresión generadora a una expresión (sin paréntesis)
import math
suma = sum(valor*valor for valor in range(4))
print(f'Resultado suma: {suma}')


# también podemos usar una lista o cualquier otro iterador
lista = ['Juan', 'Perez']
generador = (valor for valor in lista)

print(next(generador))
print(next(generador))

# crear un string a partir de un generador, creado a partir de una lista
lista = ['Karla', 'Gomez', 'Martín']
contador = 0
def incrementar():
    global contador
    contador += 1
    return contador
# la primera parte es el yield, la segunda partes es el for entré paréntesis
generador = (f'{incrementar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generada: {cadena}')