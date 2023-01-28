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
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id=%s'
            valores = (
                ('José Martín', 'Zayas Zermeño', 'jmartinzayasz@gmail.com', input('Coloca id a modificar: ')),
                ('José Martín', 'Zayas Zermeño', 'jmartinzayasz@gmail.com', input('Coloca id a modificar: ')),
                ('José Martín', 'Zayas Zermeño', 'jmartinzayasz@gmail.com', input('Coloca id a modificar: '))
            )

            cursor.executemany(sentencia, valores)
            # conexion.commit()
            registros_actualizados= cursor.rowcount
            print(f'Registros actualizados {registros_actualizados}')


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
