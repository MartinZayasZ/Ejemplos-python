
# Un set es una colección de elementos únicos y es mutable
# Los elementos de un set deben ser inmutables
# conjunto = {[1,2], [3,4]}
conjunto = {'Juan', True, 18.0}
print(conjunto)

# Set vacío
# conjunto = {} genera un dict vacío
# print(type(conjunto))

# Set vacío correctamente
conjunto = set()
print(conjunto)
print(type(conjunto))

#mutable
conjunto.add('Juan')
print(conjunto)
#Contiene valores únicos
conjunto.add('Juan')
print(conjunto)
#crear un set a partir de un iterable
conjunto = set([1,4,5,7,4,8])
print(conjunto)

# podemos agregar más elementos o incluso otro set
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

#copiar un set (copia poca profunda, solo copia referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)

#verificar igualdad
print(f'Es igual en conteido ?: {conjunto == conjunto_copia}')
print(f'Es la misma referecia?: {conjunto is conjunto_copia}')

# Operaciones de conjuntos con set
# personas con distintas caracteristicas
pelo_negro = {'Juan', 'Karla', 'Pedro', 'María'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menos_30 = {'Juan', 'Karla', 'María'}
# Todos con ojos cafe y pelo rubio(union) (no se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))
# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))
# Intersection, Sólo personas con ojos cafe y pelo rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))
# Difference, Pelo negro sin ojos cafe (no conmutativa)
print(pelo_negro.difference(ojos_cafe))
# diferencia simétrica, pelo negro u ojos cafes pero no ambos (comutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

