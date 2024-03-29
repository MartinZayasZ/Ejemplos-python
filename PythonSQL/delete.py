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
            sentencia = 'DELETE FROM persona WHERE id=%s'
            valores = (input('Coloca id para eliminar: '),)
            cursor.execute(sentencia, valores)
            # conexion.commit()
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados {registros_eliminados}')


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
