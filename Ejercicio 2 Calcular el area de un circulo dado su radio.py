"""
Programa: Ejercicio 2, calcular el Área de un círculo dado su radio, el A = PI * radio al cuadrado
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
PI = 3.14159265  #Constante PI 

#Necesitamos el radio, podemos hacerlo con una variable o en una segunda versión, solicitando el valor por consola
radio = 5

area = PI * (radio * radio)
print("El area de un círculo con radio %3.2f" % radio ,"es: %2.3f" % area, end="\n")

#   Segunda versión solicitando el radio por consola    ##########################################################
radio = float(input("Introduce el radio de la circunferencia: "))

area = PI * (radio * radio)
print("El area de un círculo con radio %3.2f" % radio ,"es: %2.3f" % area, end="\n")