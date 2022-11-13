import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo grid')
ventana.iconbitmap('icono.ico')

def evento1():
    boton1.config(text='Botón 1 presionado')
def evento2():
    boton2.config(text='Botón 2 presionado')

#definimos dos botones
boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(row=0, column=0, sticky='W')

# N(arriba), E(derecha), S(abajo), W(izquierda),
boton2 = ttk.Button(ventana, text='Botón 2', command=evento2)
boton2.grid(row=1, column=0, sticky='WE')

ventana.mainloop()