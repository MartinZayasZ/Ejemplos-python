# GUI - Graphical User Interface
# Tkinter - TK Interface
# Importamos el módulo de tkinter

import tkinter as tk
from tkinter import ttk

# creamos un objeto usando la clase tk

ventana = tk.Tk()

# Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('600x400')

#Cambiamos el nombre de la ventana
ventana.title('Tkinter')

# cambios el icono
ventana.iconbitmap('icono.ico')

# creamos un método de evento
def evento_click():
    boton1.config(text='Botón presionado')
    print('Ejecuón del evento_click')
    #creamos un nuevo componente
    boton2 = ttk.Button(ventana, text='Nuevo botón', command=evento_click)
    boton2.pack()


# Creamos un boton (widget o componente) el objeto padre es la ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)
# utilizar el pack layout manager para mostrar el boton de la ventana
boton1.pack()





# Iniciamos la ventana (esta línea la ejecutamos al final)
# Si la ejecutamos antes, no se mostraran los cambios
ventana.mainloop()