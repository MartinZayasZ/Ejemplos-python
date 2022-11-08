class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# mostrar los atributos de un objeto
persona1 = Persona('Juan', 'Perez')
print(persona1.__dict__)

# crear un atributo live
print(persona1.contador_personas)
persona1.contador_personas = 10
print(persona1.contador_personas)
print(persona1.__dict__)

#El atributo anterior oculta al atributo de clase
Persona.contador_personas += 1
print(Persona.contador_personas)

# un segundo objeto
persona2 = Persona('Martín', 'Zayas')
print(persona2.__dict__)
Persona.contador_personas += 1
print(Persona.contador_personas)

# Asociar un atributo de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2)