class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id = self.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id} {self.nombre} {self.edad}]'

persona1 = Persona('Martin', 27)
print(persona1)

persona2 = Persona('Laura', 27)
print(persona2)

persona3 = Persona('Iván', 27)
print(persona3)
print(Persona.contador_personas)