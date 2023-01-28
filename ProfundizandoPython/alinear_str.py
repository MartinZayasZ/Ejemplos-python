# Alinear cadenas
# centrar un str

titulo = 'Sitio web de GlobalMentoring.com.mx'

print(titulo.center(len(titulo)+50, '\u2665'))

print(titulo.ljust(len(titulo)+50, '\u2665'))
print(titulo.rjust(len(titulo)+50, '\u2665'))

# Reemplazar contenido en un str

print(titulo.replace(' ', '-'))

# Eliminar caracteres al inicio y final - strip
titulo = ' *** GlobalMentoring *** '
print(f'cadena original:',titulo, len(titulo))
titulo = titulo.strip()
print(f'cadena strip:',titulo, len(titulo))