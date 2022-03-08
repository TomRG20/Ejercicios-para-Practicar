"""
Programa: Ejercicio 9, programa que dado un número nos diga si es negativo, positivo o si vale cero
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
#Constantes 
POS  = "POSITIVO"
NEG  = "NEGATIVO"
ZERO = "CERO"

# Lo primero que haremos es solicitar por consola un número entero (puede ser negativo)
num = int(input("Introduce un número: "))

if( num < 0):
    print("El número introducido es: ", NEG)
elif(num > 0):
    print("El número introducido es: ", POS)
else:
    print("El número introducido es: ", ZERO)
