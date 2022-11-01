import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = (
                ('Roberto', 'Lara', 'clara@gmail.com'),
                ('XX', 'Lara', 'clara@gmail.com'),
                ('Loco', 'Lara', 'clara@gmail.com')
            )

            cursor.executemany(sentencia, valores)
            #conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros insertados {registros_insertados}')

            # sentencia = 'SELECT * FROM persona WHERE id IN %s'
            # id_persona = 1
            # #llaves_primarias = ((1, 2),)
            # entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
            # llaves_primarias = (tuple(entrada.split(',')),)
            #
            # cursor.execute(sentencia, llaves_primarias)
            # registros = cursor.fetchall()
            # for registro in registros:
            #     print(registro)

           # print(registros)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
