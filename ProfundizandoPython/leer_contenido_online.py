import urllib.request

req = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

# with urllib.request.urlopen(req) as mensaje:
#     contenido = mensaje.read().decode('UTF-8')
#     print(contenido)
#
#
# with open('nuevo_archivo.txt', 'w', encoding='UTF-8') as archivo:
#     archivo.write(contenido)

palabras = []
with urllib.request.urlopen(req) as mensaje:
    for linea in mensaje:
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)

print(len(palabras))
