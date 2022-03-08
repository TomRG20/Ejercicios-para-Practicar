""" Ejercicio sobre variables
    @Autor: Tomás Rodríguez
    @Fecha: 19/07/2021
    
    Variables: Etiquetas a las que podemos asignar valores. 
    
    @nota: Reglas al nombrar y usar variables en python:
    -------Los nombres de las variables solo pueden contener letras, números y guiones bajos. 
    -------Los nombres de las variables pueden empezar por una letra o un guión, pero no por un número. 
    -------Los espacios no estan permitidos, usar los guiones para separar las palabras.
    -------Evitar usar palabras clave o reservadas por el sistema. 
    -------Los nombres de las variables deberian ser cortos pero descriptivos. 
    -------Usar letra minuscula. 
    
    Constantes, son variables en las que su valor es fijo y no puede cambiarse
                se representan con nombres en mayuscula. Por ejemplo: 
                MAX_VALUE = 5000
    
    # Comentarios
    \t Tabulación
    \n Nueva línea 
"""
#BOOLEANOS

verdadero = True
falso = False

print(verdadero)
print(falso)

#CADENAS 

mensaje  = "Hola esto es una variable de tipo cadena "
mensaje2 = 'Hola esto tambien es una variable de tipo cadena '
mensaje3 = "  El lenguaje 'Python' me permite pirulas como estas en las cadenas  "


#métodos para trabajar con cadenas: (los métodos son acciones)

#MAYUS or MINUS 
print(mensaje.title())  #en este caso title es un método que cambia la letra inicial a mayuscula de cada palabra del mensaje
print(mensaje.capitalize()) #en este caso capitalize es un método que cambia a mayus solo la primera letra de la cadena
print(mensaje.swapcase()) #me cambia las letras en minuscula a mayuscula y viceversa
print(mensaje.casefold()) #como el lower pero más profesional y teniendo en cuenta casos especiales
print(mensaje2.upper()) #me pone todo a mayuscula
print(mensaje3.lower()) #me pone todo a minuscula

#Eliminar Espacios en BLANCO tanto delante como detrás del texto
print(mensaje3.strip())  #me quita por los dos lados
print(mensaje3.lstrip()) #me los quita del inicio
print(mensaje3.rstrip()) #me los quita del final

#sustitución, busqueda, separación
print(mensaje3.find("de")) #me busca esa palabra en la cadena y te dice el indice donde está o -1 sino está 
print(mensaje3.count("de")) #me cuenta esa palabra en la cadena cuantas veces aparece y nos devuelve un entero 
print(mensaje3.replace("d", "t")) #si necesitas reemplazar una cadena por otra lo hace tantas veces como d existan
print(mensaje.split("-")) #es un separador, crea una lista con cada elemento
print(mensaje.startswith("-")) #devuelve True si la cadena empieza con el guion
print(mensaje.endswith("?-")) #devuelve True si la cadena termina con ?-

#USO de variables en cadenas, puede que deseemos que dos variables representen un nombre y un apellido y combinarlos
nombre = 'Tomás'
Apellido = 'Rodríguez'

nombre_completo = f"{nombre} {Apellido}"
print(f"Hola, {nombre_completo}! Bienvenido a esta introducción")


#NÚMEROS

#Enteros 
num1 = 3
num2 = 5
print("La suma de los 2 numeros es: ", num1 + num2)
print("La resta de los 2 numeros es: ", num2 - num1)
print("La multiplicación de los 2 numeros es: ", num1 * num2)
print("La división de los 2 numeros es: ", num2 / num1)

#Flotantes, cualquier número con un punto decimal
num1 = 3.5 
num2 = 5.3 
print("La suma de los 2 numeros es: ", num1 + num2)
print("La resta de los 2 numeros es: ", num2 - num1)
print("La multiplicación de los 2 numeros es: ", num1 * num2)
print("La división de los 2 numeros es: ", num2 / num1)

#Asignación Múltiple
num1, num2, num3 = 0,2,3 
print(num1)
print(num2)
print(num3)
