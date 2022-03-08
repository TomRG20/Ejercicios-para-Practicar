'''
Programita para probar la ordenación de Tuplas y Diccionarios, usando las funciones normales
y el uso de KEY para iniciar el valor de ordenación. 

reverse, sort, sorted, key

key: debe tomar un único argumento y devolver una clave, que será el valor para realizar la ordenación

'''

#tupla de tuplas (nombre, edad, dni, sexo)
personas = (
    ('Maria', '42', '30057342-H', 'M'),
    ('Juan', '36', '21456793-M', 'H'),
    ('Paco', '67', '34821678-D', 'H'),
    ('Julia', '22', '06744674-S', 'M'),
    ('Silvia', '35', '86564235-F', 'M')
)

print("\n", personas[0][0]) #devuelve Maria

print(personas)

#diccionario de diccionarios de personitas
personitas = {0:{"Nombre":'Maria', "Edad":42, "Dni":'30057342-H', "Sexo":'M'},
              1:{"Nombre":'Juan', "Edad":36, "Dni":'21456793-M', "Sexo":'H'},
              2:{"Nombre":'Paco', "Edad":67, "Dni":'34821678-D', "Sexo":'H'},
              3:{"Nombre":'Julia', "Edad":22, "Dni":'06744674-S', "Sexo":'M'},
              4:{"Nombre":'Silvia', "Edad":35, "Dni":'86564235-F', "Sexo":'M'}              
              }

print("\n ", personitas[0]["Nombre"]) #devuelve Maria

print(personitas)


#Personas ordenadas por DNI:

#Personas ordenadas por Nombre:

#Personas ordenadas por Edad:

#Personas ordenadas por Sexo:



#Personitas ordenadas por DNI:

#Personitas ordenadas por Nombre:

#Personitas ordenadas por Edad:

#Personitas ordenadas por Sexo:

