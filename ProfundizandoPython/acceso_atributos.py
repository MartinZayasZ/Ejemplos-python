# Ejemplo atributos publicos, protegidos, privados

class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado


objeto = MiClase('Valor publico', 'Valor protegido', 'Valor privado')
#acceder al atributo público
print(objeto.publico)
# modificar el valor público
objeto.publico = 'Nuevo valor público'
print(objeto.publico)

# acceso al valor protegido
print(objeto._protegido)
# Modificar atributo protegido
objeto._protegido = 'Nuevo valor protegido'
print(objeto._protegido)

# # acceso al valor privado
# print(objeto.__privado)
# # Modificar atributo privado
# objeto.__privado = 'Nuevo valor privado'
# print(objeto.__privado)

print(objeto._MiClase__privado)
#modificar valor privado
objeto._MiClase__privado = 'Nuevo valor privado'
print(objeto._MiClase__privado)