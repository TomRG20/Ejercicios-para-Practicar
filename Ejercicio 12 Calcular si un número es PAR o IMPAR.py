"""
Programa: Ejercicio 12, calcular si un número es PAR o IMPAR, es par si el resto de la división por 2 es 0
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
#Lo primero que haremos es solicitar por consola el número que deseamos saber si es par o impar
num = int(input("Introduce un número entero: "))

# Ahora hacemos la operación para sacar el resto de la división y si da 0 es par. 
if ( (num % 2) == 0 ):
    print("El número %d" %num, "es PAR")
else: 
    print("El número %d" %num, "es IMPAR")
