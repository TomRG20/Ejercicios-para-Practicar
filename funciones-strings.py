# Funciones en strings
string = "hola mundo"
string2 ="********* python es el mejor **********"
lista = ["uno", "dos", "tres", "cuatro"]
sep = "/"

# convierte la primera letra en mayuscula
print("Funcion capitalize: ", string.capitalize())  
print("Funcion upper: ", string.upper())  # convierte el string en mayusculas
print("Funcion lower: ", string.lower())  # convierte el string en minusculas
print("Funcion len: ", len(string))  # obtiene la longitud de un string, cuenta los espacios

# nos hace una lista con un separador indicado como argumento
print("Funcion split: ", string.split(" "))
 
# reemplazar subcadenas, antigua por la nueva, el 1 es el numero de reemplazos que deseamos
print("Funcion replace: ", string.replace("o", "O",1)) 
print("Funcion replace: ", string.replace("o", "O"))  # reemplazar subcadenas, antigua por la nueva
# cuenta el numero de veces que aparece un subcadena, desde la pos 0 hasta el final
print("Funcion count: ", string.count("h", 0, len(string))) 

print("Funcion lstrip: ", string2.lstrip("*"))  # eliminar los caracteres del principio del string
print("Funcion rstrip: ", string2.rstrip("*"))  # eliminar los caracteres del final del string

# pocicion index de la primera pos de una subcadena
print("Funcion find: ", string.find("mundo", 0, len(string))) 
# posicion index de la primera pos de una subcaneda de derecha a izquierda
print("Funcion rfind: ", string.rfind("ndo", 0, len(string)))

# nos devuelve un valor verdadero o falso si el string contiene digitos o no
print("Funcion isdigit: ",string.isdigit()) 

# convierte un array en un string a traves de un separador indicado
print("Funcion join: ", sep.join(lista))