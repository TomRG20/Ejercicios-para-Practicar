"""
Programa: Ejercicio ejemplo de listas:
          a)  Crear una lista e inicializarla con 5 cadenas de caracteres leidas por teclado.
          b)  Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla. 
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 04 de Enero de 2021
"""

# parte (a) del ejercicio: 
mi_lista = []

for x in range(5):   
    dato= input("Introduce un dato:")
    mi_lista.append(dato)

print("Mi lista es: ", mi_lista)

# parte (b) del ejercicio:
mi_lista.reverse()
nueva_lista = mi_lista #Esto tiene un fallo y es que ambos punteros apuntan a la misma lista, cualquier cambio en uno modifica los 2.
print ("\nMi nueva lista es: ", nueva_lista)

nueva_lista2 = mi_lista.copy() #Para arreglar el anterior fallo sería más recomendable hacer una copia en otra lista y no estarian vinculados
nueva_lista2.reverse() #la pongo como la inicial solo para ver que la original ya no esta vinculada a esta y daran listas diferentes
print("\nLa nueva copia de la lista es:", nueva_lista2)
print("\nEl original es:", mi_lista)