"""
Programa: Ejercicio 11, Decir si un caracter es un parentesis o prueba otra vez
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
# Constantes
PARENTESIS = "Es paréntesis"
JUEGA_OTRA_VEZ = "Prueba otra vez"

# Lo primero que haremos es solicitar por consola el caracter
caracter = input("Introduce un caracter: ")

if( caracter == "(" or caracter == ")" ):
    print(PARENTESIS)
else:
    print(JUEGA_OTRA_VEZ)
