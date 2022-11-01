class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def edad(self):
        return self._edad

    def __str__(self):
        return f'Persona: {self.nombre} {self.edad}'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo
    def __str__(self):
        return f'{super().__str__()}, Sueldo: {self._sueldo}'

if __name__ == '__main__':
    empleado1 = Empleado('Martín', 27, 50)
    print(empleado1.nombre)
    print(empleado1.edad)
    print(empleado1.sueldo)