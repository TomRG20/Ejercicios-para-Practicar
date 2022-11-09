""" Ejercicio de listas
    @Autor: Tomás Rodríguez
    @Fecha: 19/07/2021
    
    Listas. ¿Qué es una lista? ¿Como se representa?  Son MUTABLES, podemos modificar su contenido
            Una lista es una colección de elementos en un orden particular, puede incluir letras del abecedario, números, o nombres, o todo junto. 
            Podemos representar una Lista usando un nombre y a continuación unos corchetes []. Por ejemplo:
            marcas_de_coches=['mercedes','renault', 'seat']
            
            Homogéneas: Formadas por elementos de distintos tipos
            Heterogéneas: Formadas por elemenetos del mismo tipo 
"""

marcas_de_coches = ['Mercedes', 'BMW', 'Renault', 'Seat', 'WV', 'Audi', 'Skoda', 'Citroen', 'Peugeot', 'Nissan',
                    'Toyota', 'Honda', 'Ferrari', 'Porche', 'Lamborgini']
print(marcas_de_coches)  # esto nos imprime hasta los corchetes


# funcion para imprimir la lista y reutilizar código
def imprimir():
    print("\nLas marcas de coches son: ")
    for marca in marcas_de_coches:
        print(marca)


# Acceder a un valor especifico de una lista usando un indice (comienza en 0)
mensaje = f"\nLa marca de mi coche es {marcas_de_coches[9].title()}"
print(mensaje)

# Ahora veremos como modificar una lista, cambiar, añadir y eliminar elementos MÉTODOS DE LAS LISTAS

# APPEND, añade al final de la lista un elemento
marcas_de_coches.append("Kia")
imprimir()

# INSERT, añade en una posición dada un elemento
marcas_de_coches.insert(0, "Dacia")
imprimir()

# EXTEND, junta dos listas en una por decirlo así, en este caso me los añade al final
coches = ["Infiniti", "Bentley", "Jeep", "Mazda"]
marcas_de_coches.extend(coches)
imprimir()

# COPY
mar_coches = marcas_de_coches.copy()
print("\n Las marcas copiadas son: ", mar_coches)

# COUNT, cuenta las veces que el elemento elegido aparece en la lista
print(marcas_de_coches.count("BMW"))

# LEN, nos da la longitud de la lista
print("\nEl número de marcas en la lista es: ", len(marcas_de_coches))
print("\nEl número de marcas en la lista copiada es: ", len(mar_coches))

# INDEX, nos devuelve el indice que ocupa en la lista el elemento dado
print(marcas_de_coches.index("Dacia"))

# REVERSE, nos da la vuelta a nuestra lista
marcas_de_coches.reverse()
imprimir()

# SORT, nos ordena la lista
marcas_de_coches.sort()
imprimir()
mar_coches = marcas_de_coches.copy()
print(mar_coches)

# SORTED, nos ordena una lista temporalmente, sin afectar al orden real de la lista


# Ahora trabajaremos con mar_coches para no cargarnos la lista inicial ya llena y la iremos comprobando conforme vamos eliminandola

# DEL, elimina la posición dada entre corchetes de la lista, este elemento borrado es irrecuperable
del mar_coches[0]
print(mar_coches)

# POP ,elimina la posición dada entre corchetes de la lista, pero con la diferencia de que ese elemento borrado te lo da para trabajar
mar_coches.pop(0)
borrado = mar_coches.pop(7)
print(borrado)  # elemento borrado que ahora esta en una variable que puede reutilizar
print(mar_coches)

# REMOVE, elimina la primera occurrencia de un elemento que este en la lista
mar_coches.remove("Mazda")
print(mar_coches)

# CLEAR, elimina toda la lista completa dejandola en blanco
mar_coches.clear()
print(mar_coches)

imprimir()  # lista original

# lista vacia
miLista = []

miLista = [1, 2, 3, 4, 5, 6]  # lista númerica, homogénea

print(len(miLista))  # me devuelve el tamaño

print(miLista[0:3])  # me imprime los 4 primeros elementos
print(miLista[0])  # me imprime el primer elemento

miLista[0] = "20"





def ordenamientoburbuja(mi_lista2):
    for paso in range(len(mi_lista2) - 1, 0, -1):
        for i in range(paso):
            if mi_lista2[i] > mi_lista2[i + 1]:
                temp = mi_lista2[i]
                mi_lista2[i] = mi_lista2[i + 1]
                mi_lista2[i + 1] = temp


mi_lista2 = [17, 2, 13, 4, 25, 6, 1, 14]  # lista númerica desordenada, homogénea
ordenamientoburbuja(mi_lista2)
print(mi_lista2)

