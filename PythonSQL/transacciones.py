import psycopg2 as db

conexion = db.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db')

try:
    conexion.autocommit = False
    cursor = conexion.cursor()

    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('José', 'Zayas Zermeño', 'mzayas@somos.mx')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s WHERE id=%s'
    valores = ('JUAN', 'X2', 3)
    cursor.execute(sentencia, valores)

    conexion.commit()

    print('Termino la transacción, se hizo commit!')


except Exception as e:
    print(f'Ocurrio un error, se hizo rollback: {e}')
    conexion.rollback()
finally:
    conexion.close()
