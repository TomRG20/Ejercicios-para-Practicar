""" Ejercicio de prueba
    @Autor: Tomás Rodríguez
    @Fecha: 26/07/2021
    
    Diccionarios. ¿Qué son?
    Es una estructura que permite almacenar su contenido en forma de llave y valor
    
    Se crean usando {} separando con una coma cada par key:value, por ejemplo:
    
    diccionario = {"nombre" : "Sara", "Edad" : 27, "Sexo" : "Mujer"}
    
    Son dinámicos, pueden crecer o decrecer, se pueden añadir o eliminar elementos
    Son indexados, los elementos del diccionario son accesibles a través del key
    Son anidados, un diccionario puede contener a otro diccionario en su campo value
    Los diccionarios se pueden anidar d = {"a": 1 , "b": 2}  e = {"c": 3 , "d": 4} 
    c ={"A" : d, "B" : e} 
    
""" 
#Como crear un diccionario en python (3 formas de crearlos, dos de ellas usando un constructor dict)
d1 = {"Nombre" : "Sara", "Edad" : 27, "Sexo" : "Mujer"}

d2 = dict([('Nombre', 'Pepe'),("Edad", 28), ('Sexo', "Varón"), ])

d3 = dict(Nombre ='Ana', Edad = 37, Sexo = 'Mujer')


print(d1)  # {'Nombre': 'Sara', 'Edad': 27, 'Sexo': 'Mujer'}
print(d2)  # {'Nombre': 'Pepe', 'Edad': 28, 'Sexo': 'Varón'}
print(d3)  # {'Nombre': 'Ana', 'Edad': 37, 'Sexo': 'Mujer'}


# Imprime los key del diccionario
for x in d1:
    print(x)

# Impre los value del diccionario
for x in d1:
    print(d1[x])

# Imprime los key y value del diccionario
for x, y in d1.items():
    print(x, y)


#Acceder y modificar los valores del diccionario
print(d1["Nombre"])
print(d1.get("Edad"))

d1["Nombre"] = "Laura"  #cambio Sara por Laura
print(d1)

#Metodos de los diccionarios 

#el metodo clear() elimina todo el contenido del diccionario
s = {'a': 1, 'b': 2}
s.clear()
print(s)

#el metodo get() nos permite consultar el value para un key dado, hay un segundo parametro que es un valor por defecto si no encuentra la key
s = {'a': 1, 'b': 2}
print(s.get('a'))
print(s.get('z', 'No encontrado'))

#el metodo items() devuelve una lista con los keys y los values del diccionario. Si se convierte en list se puede indezar como si de una lista normal se tratase
#siendo los primeros elementos las key y los segundos los value
s = {'a': 1, 'b': 2}
k = s.items()
print(k)              # dict_items([('a', 1), ('b', 2)])
print(list(k))        # [('a', 1), ('b', 2)]
print(list(k)[0][0])  # a

#el metodo keys() devuelve una lista con todas las keys del diccionario
d = {'a': 1, 'b': 2}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']

#el metodo values() devuelve una lista con todos los values o valores del diccionario
d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]

#el metodo POP() busca y elimina la key que se pasa como parametro y devuelve su valor asociado, tambien puede devolver un valor por defecto en caso de ser null
d = {'a': 1, 'b': 2}
d.pop('a')
print(d) #{'b': 2}
d = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4}
d.pop('c', -1)
print(d) #{'a': 1, 'b': 2, 'd': 4}

#el metodo popitem() elimina de manera aleatoria un elemento del diccionario
d = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4}
d.popitem()
print(d) #{'a': 1, 'b': 2, 'c': 3}

#el metodo update() se llama sobre un diccionario y tiene como entrada otro diccionario, los value son actualizados y si alguna key del nuevo diccionario no está, es añadida
d = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4}
d2 = {'a': 3, 'c': 1}
d.update(d2)
print(d) #{'a': 3, 'b': 2, 'c': 1, 'd': 4}
