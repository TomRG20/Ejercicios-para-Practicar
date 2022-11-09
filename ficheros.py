#Escribir y leer ficheros en python

#MODOS: 
# w : escritura, crear el fichero si no existe, si existe el fichero reemplaza el contenido.
# a : escritura, crear el fichero si no existe, si existe agrega el nuevo contenido al final. 
# r : lectura de los ficheros 

# creamos el manejador para crear un archivo HTML
manejador = open("index.html", "w") 

html = "<!DOCTYPE HTML>\n"
html += "<html>\n"
html += "<head>\n"
html += "<title>Hola mundo</title>\n"
html += "</head>\n"
html += "<body>\n"
html += "<h1>Hola mundo</h1>\n"
html += "</body>\n"
html += "</html>\n"

# Escribimos en el fichero
manejador.write(html)
manejador.close()

print("\n *** Documento HTML creado con exito ***")

# Leemos el fichero
print("\n *** Ahora vamos a leer el archivo con la funcion r ***")

manejador = open("index.html", "r")
contenido = manejador.read()

print(contenido)
manejador.close()

# Leemos el fichero linea a linea a traves de un bucle for
manejador = open("index.html", "r")
for linea in manejador: 
    print(linea, end="") 

manejador.close()