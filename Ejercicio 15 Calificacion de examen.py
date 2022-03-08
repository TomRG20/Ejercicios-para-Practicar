"""
Programa: Ejercicio 15, Programa que te califica en texto una nota de un examen pasada por consola
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
# Lo primero pediremos la nota por consola, podemos meter una nota real, por ejemplo 5.5
nota = float(input("Introduce una nota: "))

if( nota < 5 ): 
    print("La nota es: Suspenso")
if( nota >= 5 and nota < 7 ):
    print("La nota es: Aprobado")
if( nota >= 7 and nota < 8.5 ):
    print("La nota es: Notable")
if( nota >= 8.5 and nota < 10 ):
    print("La nota es: Sobresaliente")
if( nota == 10 ):
    print("La nota es: Matricula de honor") 