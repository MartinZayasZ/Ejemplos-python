# Profundizando en el tipo float

a = 3.0
print(f'a: {a:.2f}')

# Constructor float puede recibir int y str
b = float(10)
print(f'b: {b:.2f}')

c = float('10')
print(f'c: {c:.2f}')


# Notación exponencial (valores positivos o negativos)
a = 3e5
print(f'a: {a:.2f}')

a = 3e-5
print(f'a: {a:.5f}')