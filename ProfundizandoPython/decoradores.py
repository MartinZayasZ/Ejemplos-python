
# un decorador es una función que recibe una funcion y regresa otra
# lo utilizamos para extender funcionalidad

# función decorador
# 1. funmciíon decorador(a)
# 2. función a decorar (b)
# 3. función decorada (c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print('Antes de ejecutar la función')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Después de ejecutar la función')
        return resultado
    return funcion_decorada_c

@funcion_decorador_a
def sumar(a, b):
    return a+b

resultado = sumar(10, 5)
print(f'Resultado: {resultado}')