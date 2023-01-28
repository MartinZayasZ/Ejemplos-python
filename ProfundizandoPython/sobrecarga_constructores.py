# Simulación de sobrecarga de constructories
# otras formas de crear objetos

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    @classmethod
    def crear_persona_con_valores(cls, nombre, apellido):
        return cls(nombre, apellido)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'


persona1 = Persona('Martín', 'Zayas')
persona_vacia = Persona.crear_persona_vacia()
print(persona_vacia)

person_con_valores = Persona.crear_persona_con_valores('Karla', 'gomez')
print(person_con_valores)