""" Ejercicio de prueba
    @Autor: Tomás Rodríguez
    @Fecha: 24/05/2021
    
    Tuplas. ¿Qué son?
    Es similar a una lista, pero es INMUTABLE, una vez inicializada ya no se puede cambiar ninguno de sus elementos sin generar un nuevo objeto
    
    se representan con parentesis en vez de corchetes (e1, e2, e3)
    Para convertir a tipo tuplas, hay que usar la funcion tuple() 
    
    
"""

#Tupla semana
semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")  
semana_laboral = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")

Horario =("10:00 - 14:00", "16:00-20:00")


#funcion para imprimirme todas las tuplas
def imprimir(tup):
    for t in tup:
        print("\t", t, end=" ")



imprimir(semana)

print("\n")
for dia in semana_laboral:
    pos = semana.index(dia)
    
    print(pos, end=" ")


print("\n")
#convertir listas en tuplas usando la función de tuple()
lista = [1,2,3]
tupla = tuple(lista)
print(type(tupla)) 
print(tupla)


#Se puede iterar una tupla de la misma manera que una lista
tupla = (1,2,3,4)
for t in tupla:
    print(t)

#Metodos de tuplas
l = (1, 2, 3, 3, 3, 4, 5)
print(l.count(3))                 # me dice el numero de veces que aparece en la tupla dicho elemento 3

print(l.index(3))                 # busca el objeto que se le pasa como parámetro y devuelve el indice de su pos, o valueError si no lo encuentra
print(l.index(3, 3))              # me busca el objeto, y el segundo parametro me dice a partir de que indice empezara a buscar el objeto

