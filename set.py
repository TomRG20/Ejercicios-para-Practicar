""" Ejercicio de prueba
    @Autor: Tomás Rodríguez
    @Fecha: 26/07/2021
    
    Set. ¿Qué son?
    Son una estructura de datos similar a las listas, que permiten almacenar elementos con unas diferencias:
    
    1. los elementos de un set son únicos, lo que significa que no pueden haber elementos duplicados
    2. los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados
    3. sus elementos deben ser inmutables (como las tuplas)
    
    Es importante entender conceptos matemáticos como la teoría de conjuntos. 
    
    Para crear un set, utilizaremos set() y pasando como entrada cualquier tipo iterable. 
    O usando {} en vez de set
    
    s = set([1,3,5,7])
    
    Si ponemos dentro del set dos elementos repetidos solo tomara uno de ellos
    s = set([1,3,5,5,7]) solo tomara un 5
    
    Los set son inmutables, no podemos acceder a sus datos con su indice.
    

"""
s1 = set([1,3,5,7])
s2 = {2,4,6,8}
s3 = {2,2,3,3,4,4,5,5}

#iterar sets: 
for s in s1:
    print(s)

#funcion len()
print("El tamaño de s es:", len(s1))

#saber si un valor está en el set o no
print("El valor 4 esta en el set s1? :", 4 in s1)  #en este caso me devuelve falso

#union de varios sets, operador | me une 2 sets sin repetir elementos y ordenados
print(s2 | s3) 

#añadir un elemento al set ADD() ya me lo devuelve ordenado
s2.add(10)
s2.add(0)
print(s2)

#eliminar un elemento que se pasa como parametros, si no lo encuentra dará error REMOVE()
s2.remove(0)
print(s2)

#el metodo DISCARD() es muy parecido al remove, pero si no se encuentra el elemento no hace nada
s2.discard(0)
print(s2)

#eliminar un elemento aleatorio del set POP()
s3.pop()
print(s3)

#eliminar todos los elementos del set CLEAR()
s4 = {1,2,3}
s4.clear()
print(s4) #me devuelve set()

#OTROS metodos
print("La union entre s1 y s2 es: ", s1.union(s2))
print("La intersección entre s1 y s2 es: ", s1.intersection(s2))
print("La diferencia entre s1 y s2 es: ", s1.difference(s2))
print("La diferencia simetrica entre s1 y s2 es: ", s1.symmetric_difference(s2)) #devuelve la diferencia simetrica del conjunto con el s2 como un conjunto nuevo
print("Es un conjunto disjunto? : ",s1.isdisjoint(s2)) #Dos conjuntos A y B son disjuntos si no tienen elementos en común, es decir, la intersección de A y B es el conjunto vacío
print("Es un subconjunto de s2? : ", s1.issubset(s2)) #devuelve true si el conjunto es subconjunto del s2
print("Es un superconjunto de s2? : ", s1.issuperset(s2)) #devuelve true si el conjunto es superconjunto del s2
print("El nuevo conjunto después de la unión es : ", s1.update(s2))  #actualiza el conjunto tras realizar la union con el s2
print("El nuevo conjunto después de la intersección es : ", s1.intersection_update(s2)) #actualiza el conjunto tras realizar la intersección con el s2
print("El nuevo conjunto después de la diferencia es : ", s1.difference_update(s2))  #actualiza el conjunto tras realizar la diferencia con el s2
print("El nuevo conjunto después de la diferencia simetrica es : ", s1.symmetric_difference_update(s2))  #actualiza el conjunto tras realizar la diferencia simetrica con el s2

