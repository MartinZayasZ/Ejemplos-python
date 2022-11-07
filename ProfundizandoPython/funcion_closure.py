# Un closure es una función que define a otra, y además la regresa
# la función anidada puede acceder a las variables locales definidas
# en la función principal o externa


# función principal
def operacion(a, b):
    # definimos una función interna o anidada
    def sumar():
        return a + b
    # Retornar la función
    return sumar

mi_funcion_closure = operacion(5, 2)
print(f'Resultado: {mi_funcion_closure()}')

# llamar la función regresada al vuelo
print(f'Resultado: {operacion(2, 3)()}')