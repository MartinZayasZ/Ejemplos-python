
def funcion_externa():
    variable_local_externa = 'Variable local externa'

    def funcion_anidada():
        variable_local_anidada = 'variable local anidada'

        nonlocal variable_local_externa
        variable_local_externa = 'nuevo valor, variable local externa'

    funcion_anidada()
    print(f'variable local externa: {variable_local_externa}')

funcion_externa()