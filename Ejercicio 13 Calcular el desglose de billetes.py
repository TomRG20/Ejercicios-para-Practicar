"""
Programa: Ejercicio 13, calcular el desglose en billetes y monedas de una cantidad entera dada por consola
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
########################################################################
# Como dato importante tenemos que ver que billetes y monedas tenemos: #
# ____________________________________________________________________ #
# Billetes: 500, 200, 100, 50, 20, 10 y 5 €                            #
# Monedas: 2 y 1 €                                                     #
########################################################################

cantidad = 978 #euros  *678€ era la cifra original del enunciado*

#ahora hacemos el desglose, poco a poco...

resultado_500 = cantidad // 500  #primero sacamos cuantos billetes de 500 hay con esta división entera
resto = cantidad % 500 #sacamos el resto de esa división, con este resto tendremos que seguir el desglose

resultado_200 = resto // 200  #sacamos cuantos billetes de 200 hay de lo que nos quedaba del resto de antes
resto = resto % 200 #del resto anterior sacamos el resto de esa división, con este seguiremos el desglose 

resultado_100 = resto // 100
resto = resto % 100

resultado_50 = resto // 50
resto = resto % 50

resultado_20 = resto // 20 
resto = resto % 20

resultado_10 = resto // 10
resto = resto % 10

resultado_5 = resto // 5
resto = resto % 5

resultado_2 = resto // 2
resto = resto % 2

resultado_1 = resto // 1
resto = resto % 1 


print("\nEl resultado del desglose de la cantidad de %d€ es el siguiente: \n" % cantidad)

if(resultado_500 != 0):
    print("%d Billetes de 500" % resultado_500, end="€\n")
if(resultado_200 != 0):
    print("%d Billetes de 200" % resultado_200, end="€\n")
if(resultado_100 != 0):
    print("%d Billetes de 100" % resultado_100, end="€\n")
if(resultado_50 != 0):
    print("%d Billetes de 50" % resultado_50, end="€\n")
if(resultado_20 != 0):
    print("%d Billetes de 20" % resultado_20, end="€\n")
if(resultado_10 != 0):
    print("%d Billetes de 10" % resultado_10, end="€\n")
if(resultado_5 != 0):
    print("%d Billetes de 5" % resultado_5, end="€\n")
if(resultado_2 != 0):
    print("%d Monedas de 2" % resultado_2, end="€\n")
if(resultado_1 != 0):
    print("%d Monedas de 1" % resultado_1, end="€\n")
else: 
    print()
