import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo grid')
ventana.iconbitmap('icono.ico')

#entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
#entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.DISABLED)
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.DISABLED)
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)

entrada1.grid(row=0, column=0)
# insert agrega un texto
entrada1.insert(0, 'Introduce una cadena')
entrada1.insert(5, '-')
entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly')

def enviar():
    print(entrada1.get())

# Creamos un botón
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)



entrada1.mainloop()