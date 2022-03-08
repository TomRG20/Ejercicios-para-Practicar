#Funciones para Arrays
diccionario = {"uno":1, "dos":2, "tres":3}
lista = ["uno", "dos", "tres"]
tuples = ("mundo", "python", "python", "mundo")

#devuelve el numero de elementos en arrays: list, tuples y diccionarios
print("Funcion len: ", len(diccionario)) 

lista.append("cuatro")
#agrega un nuevo elemento al final de un array list con el valor dado
print("Funcion append: ", lista) 

lista.insert(2, "cinco")
#inserta el valor antes de la posicion index x dada, solo valida para array list
print("Funcion insert: ", lista) 

lista.pop(2)
#eliminar del array el elemento a traves del index x indicado, solo valido para arrays
print("Funcion pop: ", lista) 

#busca el valor indicado en los arrays list o tuples y regresa la pos de la primera ocurrencia encontrada. 
print("Funcion index: ", tuples.index("python")) 

lista.remove("tres")
#busca la primera ocurrencia del valor dado y lo elimina, solo valido para array list
print("Funcion remove: ", lista) 

#busca el numero de ocurrencias del valor dado en los array list y tuples
print("Funcion count: ", tuples.count("mundo")) 