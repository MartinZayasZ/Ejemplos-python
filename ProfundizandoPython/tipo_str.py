from mi_clase import MiClase
# Profundizando en el tipo str

# Concatenación automática en python
# variable = 'Adios'
# mensaje = 'Hola' 'Mundo' + variable
# mensaje += 'Universidad' 'Python'
# print(mensaje.upper())



# help(MiClase)
# print(MiClase.__doc__)
# print(MiClase.__init__.__doc__)
# print(MiClase.mi_metodo.__doc__)


# help(str.join)
# tupla_str = ('hola', 'mundo', 'universidad', 'python')
# mensaje = ' '.join(tupla_str)
# print(f'mensaje: {mensaje}')
#
# lista_cursos = ['java', 'python', 'angular']
# mensaje = ', '.join(lista_cursos)
# print(f'mensaje: {mensaje}')
#
# cadena = 'holamundo'
# mensaje = '.'.join(cadena)
# print(f'mensaje: {mensaje}')
#
# diccionario = {'nombre':'Juan', 'apellido':'Perez', 'edad':'18'}
# llaves = '-'.join(diccionario.keys())
# valores = '-'.join(diccionario.values())
# print(f'llaves: {llaves}')
# print(f'valores: {valores}')


# help(str.split)
cursos = 'Java,Python,Angular,PHP'
lista_cursos = cursos.split(',')
print(f'Lista cursos: {lista_cursos}')

cursos = 'Java,Python,Angular,PHP'
lista_cursos = cursos.split(',', 2)
print(f'Lista cursos: {lista_cursos}')