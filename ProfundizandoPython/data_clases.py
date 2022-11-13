from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0

@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor de nombre vacío: {self.nombre}')


domicilio1 = Domicilio('callejon 1', 422)

persona1 = Persona('Martín', 'Zayas', domicilio1)
print(persona1)

# Variable de clase
print(f'Variable de clase: {Persona.contador_personas}')
# Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')

# Variable con valores vacíos
persona_vacia = Persona('Martín', '', None)
print(persona_vacia)

# Revisar igualdad entre objetos
persona2 = Persona('Martín', 'Zayas', domicilio1)
print(f'Objetos iguales? : {persona1 == persona2}')

# Agregar esta clase a una coleccion
coleccion = {persona1, persona2}
# Frozen = True
#print(coleccion)
#coleccion[0].nombre = 'Juan Carlos'