import pymongo

#crear y establecer conexion con miBD, mongo no creará la BD hasta crear las tablas,etc. 
micliente = pymongo.MongoClient("mongodb://localhost:27017/")

mybd = micliente["miBD"]
midoc = mybd["Usuarios"] 

'''
#-----Ahora insertaremos---------

#insertar 1 registro solo, un diccionario
miUsuario = {"_id":"01", "nombre": "Antonio", "edad": 30, "profesión": "Mecánico"}
insertar = midoc.insert_one(miUsuario)
print(insertar.inserted_id)

#insertar varios registros, una lista de diccionarios
misUsuarios = [ 
    {"_id":"02", "nombre": "Anselmo", "edad": 87, "profesión": "Jubilado"},
    {"_id":"03", "nombre": "Josefina", "edad": 88, "profesión": "Jubilada"},
    {"_id":"04", "nombre": "Anastasio", "edad": 50, "profesión": "Electricista"},
    {"_id":"05", "nombre": "Pepe", "edad": 45, "profesión": "Banquero"}
]
insertar = midoc.insert_many(misUsuarios)
print(insertar.inserted_ids)

# micliente.list_database_names() #esto me devuelve una lista de las BD
listaBD = micliente.list_database_names()
if "miBD" in listaBD:
    print("La base de datos existe")
else:
    print("la base de datos aún no existe")

''' 

#-----Ahora buscaremos---------

buscar = midoc.find_one()
print(buscar, end="\n\n")

for buscaTodo in midoc.find():
    print(buscaTodo)

# me muestra solo el registro que contenga el nombre de anastasio
for busquedaConsulta in midoc.find({"nombre": "Anastasio"}):
    print(f"\nLa consulta es: \n{busquedaConsulta}")

# si le pongo un segundo parametro, me omite lo que ponga dentro con valor 0, y muestra los de valor 1
for busquedaConsulta in midoc.find({"nombre": "Anastasio"}, {"_id": 0, "nombre": 1, "edad": 1, "profesión": 1}):
    print(f"\nLa consulta es: \n{busquedaConsulta} \n")


#-----Ahora Actualizaremos---------

consulta ={"profesión": "Pintor"}
nuevosValores ={ "$set": {"profesión": "Pintor de coches"}}
actualizar = midoc.update_one(consulta, nuevosValores)
print(actualizar.modified_count, " registros actualizados\n")

#los Jubilados tendrán la misma edad de 87
consulta ={"profesión": {"$regex" : "^J"}}
nuevosValores ={ "$set": {"edad": 87}}
actualizarTodo = midoc.update_many(consulta, nuevosValores)

print(actualizarTodo.modified_count, " registros actualizados\n")

for buscaTodo in midoc.find():
    print(buscaTodo)

#ordenar con sort
for buscaTodo in midoc.find().sort("profesión", 1):
    print(buscaTodo)


#-----Ahora Borraremos los registros---------


#eliminaré los registros que empiecen por e
consulta ={"profesión": {"$regex" : "^E"}}
borrarConsulta = midoc.delete_many(consulta)

print(borrarConsulta.deleted_count, " registros eliminados\n")

for buscaTodo in midoc.find():
    print(buscaTodo)


#-----Ahora Borraremos las tablas ---------
#midoc.drop()

# para limitar la cantidad de documentos a mostrar usaremos limit
for buscaTodo in midoc.find().limit(2):
    print(buscaTodo)
