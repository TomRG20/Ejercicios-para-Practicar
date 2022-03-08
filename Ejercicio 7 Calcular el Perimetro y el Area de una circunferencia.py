"""
Programa: Ejercicio 7, programa que me calcule el perímetro y el área de una circunferencia con dos decimales, dado un radio.
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
# tenemos que solicitar por consola el radio para hacer los calculos.
radio = float(input("Introduce el radio: "))

PI = 3.14159265

perimetro = (2 * PI) * radio
area = PI * (radio * radio)

print("El perimetro de la circunferencia es: %2.2f" % perimetro, " y el su area es: %2.2f" %area , sep=" ", end="\n")