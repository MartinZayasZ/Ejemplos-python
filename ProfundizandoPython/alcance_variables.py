# scope, alcance de variables
var_global = 'Variable global'

def imprimir():
    #para poder modificar la variable global
    global var_global
    #Acceder a una variable global
    print(f'Variable global desde función: {var_global}')
    #Definición de variable local
    var_local = 'Variable local'
    print(f'Variable local desde función: {var_local}')
    var_global = 'nuevo valor'
    # print(f'Variable global desde función: {var_global}')
    # nonlocal

# print(f'Variable local desde raíz: {var_local}')

imprimir()
print(var_global)