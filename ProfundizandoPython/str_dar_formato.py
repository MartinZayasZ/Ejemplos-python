# Dar formato a un str

nombre = 'Juan'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años '%(nombre, edad)
print(f'Mensaje: {mensaje_con_formato}')

persona = ('Martín', 'Zayas', 6300.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es de %.2f'%persona
print(f'Mensaje: {mensaje_con_formato}')



nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje_con_formato = 'Nombre {}, Edad {}, Sueldo {:.2f} '.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje_con_formato = 'Nombre {0}, Edad {1}, Sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje_con_formato = 'Nombre {nombre}, Edad {edad}, Sueldo {sueldo:.2f}'.format(edad=edad, sueldo=sueldo, nombre=nombre)
print(mensaje_con_formato)

diccionario = {'nombre':'Iván', 'edad':35, 'sueldo':8000.00}
mensaje_con_formato = 'Nombre {persona[nombre]}'.format(persona=diccionario)
print(mensaje_con_formato)