
caracteres_en_bytes = b'Hola Mundo'
print(f'Caracteres en bytes: {caracteres_en_bytes}')

mensaje = b'Universidad Python'
print(mensaje[0])
print(chr(mensaje[0]))


lista_caracteres = mensaje.split()
print(lista_caracteres)

# Convertir de str a bytes
string = 'Programación con Python'
print(f'string original: {string}')
bytes = string.encode('UTF-8')
print(f'bytes codificado: {bytes}')

# Convertir bytes a str
string2 = bytes.decode('UTF-8')
print('String decodificado', string2)

print(string == string2)