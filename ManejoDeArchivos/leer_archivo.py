try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
   # print(archivo.read())

    #print(archivo.read(3))
    #print(archivo.read(2))
    #print(archivo.readline())

    #for linea in archivo:
    #    print(linea)

    #print(archivo.readlines()[0])

    archivo2 = open('copia.txt', 'a', encoding='utf8')
    archivo2.write(archivo.read())

    archivo2.close()
    archivo.close()

    print('Proceso terminado')

except Exception as e:
    print(f'Error: {e}')