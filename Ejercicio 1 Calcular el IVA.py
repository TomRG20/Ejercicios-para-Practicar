"""
Programa: Ejercicio 1, calcular el IVA (21%) de un producto dado un precio de venta sin IVA, dado por consola o por variable precio = 25€ 
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""

# Versión 1 del programa, dado un precio por variable precio
precio = 25
#Ahora calcularemos el IVA de un precio
iva = (precio * 21) / 100 

print("\nEl IVA que hay que añadir al precio es: ", iva, "\t El precio total seria: ", iva + precio, end="\n")

################################################################################################################## 

# Versión 2 del programa, dado un precio por consola
precio = float(input("\nIntroduce un precio para calcular su IVA: "))

#Ahora calcularemos el IVA de un precio
iva = (precio * 21) / 100 
p_total = iva + precio

print("\nEl IVA que hay que añadir al precio es: ", iva, "\t El precio total seria: %3.2f " % p_total, end="\n")