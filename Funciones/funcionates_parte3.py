def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')


listarTerminos(IDE='Integrated Development Environment', PK='Primary Key')


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juan', 'Martin', 'Sergio'] #lista
desplegarNombres(nombres)
desplegarNombres((10, 2))  # tupla
desplegarNombres([10, 2])  # lista
