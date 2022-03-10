"""
1º Crea un programa que pida por pantalla los siguientes aspectos: 
-Marca de coche
-Modelo de coche 
-Año de fabricación

2º Con una funcion une marca y modelo

3º Con una funcion que marque si el coche tiene mas de 25 años y que lance un mensaje que exprese
que es un coche clasico.

@Autor: Tomás Rodríguez Garrido
@Fecha: 08/03/2021
@Version: 1.0
"""
import datetime as dt  #libreria para sacar la fecha

clasico = False
marcaCoche = input("\nIntroduce la marca del coche: ")
modeloCoche = input("\nIntroduce el modelo del coche: ")
anyoFabricacion = int(input("\nIntroduce el año de fabricación del coche: "))

def marca_modelo (marcaCo, modeloCo):
    return marcaCo + " " + modeloCo

def es_clasico(anyoFabri):
    dat = dt.datetime.now()
    anyo = int(dat.strftime('%Y')) #ya tengo el año actual
    if((anyo - anyoFabri) > 24):
        return True
    else: 
        return False    

print("\nNuestro coche es un ", marca_modelo(marcaCoche, modeloCoche))

clasico = es_clasico(anyoFabricacion)
if clasico == True: 
    print("El coche es un clásico. ")
else: 
    print("El coche no es un clásico. ")