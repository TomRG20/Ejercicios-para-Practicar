"""
Programa: Ejercicio 10, Calcular que Edad es joven entre dos edades introducidas por consola
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
# Constantes
MENOR = "es más joven"
IGUAL = "\nTienen la misma edad"

# Lo primero que haremos es solicitar por consola las edades
edad_1 = int(input("Introduce la primera edad: "))
edad_2 = int(input("Introduce la segunda edad: "))

if( edad_1 == edad_2): 
    print(IGUAL)
elif(edad_1 < edad_2):
    print("La primera persona: ", MENOR)
else: 
    print("La segunda persona es: ", MENOR)