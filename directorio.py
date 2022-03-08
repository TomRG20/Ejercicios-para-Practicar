#creamos una carpeta directorio para examinarla
import glob, os.path

#glob permite indexar en la ruta seleccionada para examinar los archivos y 
#documentos que contiene
#path es un submodulo de os, que nos permitirá entre otras cosas saber si
#un archivo o carpeta existe en la ruta indicada

todos = glob.glob("directorio/*") #devuelve una lista
print("Todos los archivos y carpetas que se encuentran en el directorio: ",todos)

archivos = []
for element in todos: 
    if(os.path.isfile(element)):  #isfile es para sacar los archivos
        archivos.append(element)
print("\nTodos los archivos del directorio:", archivos)

carpetas = []
for element in todos:
    if(os.path.isdir(element)):  #isdir es para sacar las carpetas
        carpetas.append(element)
print("\nTodas las carpetas del directorio:", carpetas)

#Esto me saca todos los txt del directorio
txt = glob.glob("directorio/*.txt")
print("\nArchivos:",txt)

#cada ? es una caracter, este ejemplo nos devolverá doc.txt al ser el único
#con 3 caracteres
txt3char = glob.glob("directorio/???.txt")
print("\nArchivos:",txt3char)

#Modulo os, crear y eliminar carpetas y archivos

