"""
Programa: Ejercicio 5, calcular el perimetro y el area de un rectángulo con lados l1 = 4 y l2 = 6
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
# Dado los lados
l1 = 4
l2 = 6

perimetro = (l1 * 2) + (l2 * 2)
area = l1 * l2
print("El Perimetro del rectangulo de lado 1= %d" %l1, "y lado 2= %d" %l2, "es: %d" % perimetro , "y su Área es: %d" % area)


# Solicitados por consola
l1 = float(input("Introduce el primer lado: "))
l2 = float(input("Introduce el segundo lado: "))

perimetro = (l1 * 2) + (l2 * 2)
area = l1 * l2
print("El Perimetro del rectangulo de lado 1= %3.2f" %l1, "y lado 2= %3.2f" %l2, "es: %3.2f" % perimetro , "y su Área es: %3.2f" % area)