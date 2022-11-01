from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))

    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado1 = Empleado('Martín', 6000)
imprimir_detalles(empleado1)

gerente1 = Gerente('Zulema', 5000, 'TI')
imprimir_detalles(gerente1)