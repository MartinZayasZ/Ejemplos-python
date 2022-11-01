try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Hola mundo')
    archivo.write('\nAdiós')
except Exception as e:
    print(f'Excepción {e}')
finally:
    archivo.close()