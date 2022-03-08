"""
Programa: Ejercicio ejemplo de FOR:
          Teniendo 2 cadenas, una con las vocales y otra con un texto cualquiera, calcular cuantas 
          vocales hay en la segunda cadena del texto. 
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 10 de Enero de 2021
"""

cadena_vocales = "aeiou"
cadena_ejemplo = "Hola, di Amigo y entra!"

cadena_ejemplo = cadena_ejemplo.lower() 
print(cadena_ejemplo)
contador = 0
for elementos in cadena_ejemplo:
    if(elementos in cadena_vocales):
        contador += 1

print("El número de vocales en la segunda cadena es: ", contador)