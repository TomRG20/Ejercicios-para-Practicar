"""
Esto me servirá para probar algunas clases y practicar la POO en Python

@Author: Tomás Rodríguez Garrido
@Date: 03/08/2022
@Version: 1.0
"""


class EjemploClase:
    pass


class Persona:
    # atributos de la clase
    nombre = ""
    edad = 0

    """ 
    # Constructor por defecto
    def __init__(self):
        self.nombre = "Pepe"
        self.edad = 18
    """

    # Constructor con parametros
    def __init__(self, name, years):
        self.nombre = name
        self.edad = years

    # método de la clase
    def trabajor(self):
        if self.edad < 18:
            print("Es menor de edad no puede trabajar")
        else:
            print("Es mayor de edad si puede trabajar")


obj = Persona("Angel", 36)

print("El nombre de la persona es: " + getattr(obj, 'nombre') + " y su edad es: ", obj.edad)

setattr(obj, "nombre", "pepeluis")
print(obj.nombre)

print("La edad existe? :", hasattr(obj, "edad"))  # devuelve True
print("La edad es: ", obj.edad)

delattr(obj, "edad")
print("La edad es: ", obj.edad)

