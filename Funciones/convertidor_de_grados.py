def convertir_a_fahrenheit(grados_celsius):
    return (grados_celsius * 1.8) + 32

def convertir_a_celsius(grados_fahrenheit):
    return (grados_fahrenheit - 32) / 1.8

grados_celsius = float(input('Coloque los grados celsius a convertir: \n'))
print(convertir_a_fahrenheit(grados_celsius))

grados_fahrenheit = float(input('Coloque los grados fahrenheit a convertir: \n'))
print(convertir_a_celsius(grados_fahrenheit))
