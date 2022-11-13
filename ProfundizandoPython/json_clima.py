import urllib.request
import json

req = urllib.request.Request(
    'http://globalmentoring.com.mx/api/clima.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

respuesta = urllib.request.urlopen(req)
#print(respuesta)

cuerpo_respuesta = respuesta.read()
#print(cuerpo_respuesta)
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
#print(json)

# Acceder a la descripción del clima
print(json_respuesta['clima'][0]['descripcion'])