"""
Programa: Ejercicio 16, Programa que te calcula el factorial de un número pasado por consola. (Nota: 0! = 1)
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""

#*****************************************************************************
# Notas: 
#      1º El factorial no está definido para números negativos.
#      2º El factorial de un número, se calcula multiplicando este número
#         por todos los números anteriores a él hasta el 1. Esto es:
#         
#         (Factorial de 3) 3! = 3 * 2 * 1
#         lo que nos da como resultado 6.
#         (Factorial de 6) 6! = 6 * 5 * 4 * 3 * 2 * 1
#         lo que nos da como resultado 720.
#      
#      3º Sin recursividad, ni estructuras de repetición es muy dificil
#         calcular el factorial, por lo que en este ejercicio usaremos
#         una cifra pequeña, solo para tener un ejemplo de como se hace. 
#
#*****************************************************************************

# Lo primero como siempre es pedir ese numero por consola, en este caso usaremos un numero pequeño
numero = int(input("Introduce un número inferior a 4 para factorizar: "))

# NUMERO = 3 Pondremos como ejemplo este numero para no tener que ir anidando tantos if, podriamos llegar hasta a 4
fact = 1   # El factorial siempre es 1 (Nota: 0! = 1), lo inicializamos así

""" Ahora hacemos la factorización del número, como veras hay que asegurarse que el numero no sea menos de 1 y tambien
 veras que hay un monton de sentencias condicionales anidadas una y otra vez, mientras mayor sea el número más sentencias 
 anidadas necesitaremos para sacer el factorial de ese número.
 En este ejemplo, no pasaremos del 4, porque sino se haria enorme, este se simplicará cuando veamos las estructuras de repetición
 y la recursividad """

if( numero > 1 ):
    fact = numero * ( numero - 1 )
    numero = numero -1 
    if(numero > 1):
        fact = fact * ( numero - 1 )
        numero = numero -1
        if(numero > 1):
            fact = fact * ( numero - 1 )
            numero = numero -1
            if(numero > 1):
                fact = fact * ( numero - 1 )
                numero = numero -1
                if(numero > 1):
                    fact = fact * ( numero - 1 )
                    numero = numero -1
                else: 
                    print("El factorial es: ", fact)
            else: 
                print("El factorial es: ", fact)
        else: 
            print("El factorial es: ", fact)
    else: 
        print("El factorial es: ", fact)
else: 
    print("El factorial es: ", fact)