import sys

from dao.usuario_dao import UsuarioDao
from logger_base import log
from modelos.usuario import Usuario

opcion = None

while opcion != 5:
    print('Opciones:')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')

    opcion = int(input('Escribe tu opción (1-5): '))

    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id_usuario a modificar: '))
        username_var = input('Escribe el nuevo username: ')
        password_var = input('Escribe la nueva password: ')
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDao.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDao.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
else:
    sys.exit()