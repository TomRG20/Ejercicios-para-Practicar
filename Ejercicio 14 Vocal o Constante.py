"""
Programa: Ejercicio 14, Programa que te dice si un caracter es vocal o consonante, a partir de un caracter por consola
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
# Constantes
VOCAL ="Es una vocal"
CONSONANTE = "Es una consonante"
#Podriamos crear otra constante indefinida para los elementos fuera del rango A-z pero lo dejaremos para otro programa
 
 
##################################################################
# Lo primero que tenemos que pensar es en cuales son las vocales #
# Vocales:                                                       #
#           A,a   E,e   I,i   O,o   U,u                          #
##################################################################

#solicitamos el caracter por consola

carac = input("Introduce un caracter: ")

if(carac == 'A' or carac == 'a' or carac == 'E' or carac == 'e' or carac == 'I' or carac == 'i' or carac == 'O' 
   or carac == 'o' or carac == 'U' or carac == 'u'):
    print(VOCAL)
else:
    print(CONSONANTE)
