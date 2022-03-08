"""
   Programa para crear un algoritmo:
   1- Intentare crear una lista de opciones 
   2- Le ire preguntando que inserte las opciones
   3- Compararé las opciones con una ruta feliz
   4- Si coinciden entonces habrá diseñado correctamente el algoritmo
   
   @autor: Tomás Rodríguez Garrido
   @Fecha: 14/04/21
"""
print("\n\t Hola, este programa te va a dar una serie de opciones    ",end="\n")
print("\t cuando las ordenes el programa comparará el resultado      ",end="\n")
print("\t y te dirá si has diseñado el algoritmo correctamente o no. ",end="\n")
print("\n\t Algoritmo:                                               ",end="\n")
print("\t Es una secuencia de pasos que resuelve un problema, tiene  ",end="\n")
print("\t una serie de características:                              ",end="\n")
print("\t Preciso: Tiene que resolver el problema sin errores.       ",end="\n")
print("\t Definido: La solución será siempre la misma cada ejecución.",end="\n")
print("\t Finito: Debe tener un inicio y un final.                   ",end="\n")
print("\t Legible: Cualquiera tiene que ser capaz de comprenderlo.   ",end="\n")
print("\t ---------------------------------------------------------- ",end="\n")

print("\t \t         LAVARSE LAS MANOS EN EL BAÑO: ", end="\n")
print("\n\t Opciones: ",end="\n")
print("\t****************************************************************",end="\n")

print("\t* Op 1:  Mojarse las manos por primera vez.                    *",end="\n")
print("\t* Op 2:  Enjuagarse las manos.                                 *",end="\n")
print("\t* Op 3:  Abrir el grifo del agua.                              *",end="\n")
print("\t* Op 4:  Secarse las manos.                                    *",end="\n")
print("\t* Op 5:  Aplicarse jabón en las manos.                         *",end="\n")

print("\t****************************************************************",end="\n")
print("\n\t Ahora introduce el orden correcto:                           ",end="\n")

#aqui crearemos la lista con la secuencia introducida por el alumno
OALista = []
OALista.append(int(input("\tIntroduzca la 1 opción: ")))
OALista.append(int(input("\tIntroduzca la 2 opción: ")))
OALista.append(int(input("\tIntroduzca la 3 opción: ")))
OALista.append(int(input("\tIntroduzca la 4 opción: ")))
OALista.append(int(input("\tIntroduzca la 5 opción: ")))

#Opcion correcta: 3, 1, 5, 2, 4
OCLista = [3,1,5,2,4]

if OALista == OCLista:
    print("\n\tEl algoritmo introducido es CORRECTO.\n")
else:
    print("\n\tEl algoritmo introducido es INCORRECTO. \n\t    La solución es: ", OCLista)

print("\n\n")