"""
Programa: Ejercicio 4, calcular el área de un triangulo. A = 1/2 * (b*h)
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""

#dado una altura y una base
base = 3
altura = 5

area = (base * altura) / 2
print("El área del triangulo es: %3.2f" % area)

#solicitando la altura y la base por consola
base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))

area = (base * altura) / 2
print("El área del triangulo es: %3.2f" % area)
