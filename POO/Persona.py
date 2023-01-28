class Persona:
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = args
        self.terminos = kwargs
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


persona = Persona('Martín', 'Zayas', 27, '6442329372', 2, 5, 3, m='manzana', p='pera')
persona.mostrar_detalle()
# Persona.mostrar_detalle(persona)
persona.telefono = '6442329372'
print(persona.telefono)

persona2 = Persona('Juan', 'Perez', 28)
persona2.mostrar_detalle()
