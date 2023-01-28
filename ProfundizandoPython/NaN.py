import math
from decimal import Decimal

# NaN - Not a Number, no es un número
# NaN es un tipo de dato número indefinido
a = float('NaN')
print(f'a: {a}')
print(f'Es NaN: {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN: {math.isnan(a)}')