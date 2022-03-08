"""
Programa: Ejercicio 6, programa que repita un nombre 5 veces por pantalla
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
# solicitamos el nombre por consola
nombre = input("Introduce un nombre: ")

# Repetido dejando un salto de linea entre ellos
print(nombre)
print(nombre)
print(nombre)
print(nombre)
print(nombre)

# En la misma linea pero dejando un espacio en blanco entre ellos
print(nombre, nombre, nombre, nombre, nombre)

# Otras opciones más profesionales:
print(nombre,nombre,nombre,nombre,nombre, sep="\n" , end="\n") #mete saltos de lineas en el separador
print(nombre,nombre,nombre,nombre,nombre, sep="  " , end="\n") #mete doble espacio en el separador