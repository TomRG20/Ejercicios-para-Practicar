import sqlite3, datetime
print("*** Programa para insertar regristros en la table test ***\n")

#las columnas
cadena_texto = input("Introduzca una cadena de texto: ")
entero = input("Introduzca un numero entero: ")
decimal = input("Introduzca un numero decimal: ")
#para la columna fecha lo haremos atraves de datetime

try: entero = int(entero) 
except ValueError: 
    print(entero, " no es un numero entero")
    exit() #SALE DE LA APLICACION
    
try: decimal = float(decimal) or int(decimal)
except ValueError:
    print(decimal, " no es un numero decimal")
    exit() #SALE DE LA APLICACION

#Establecer la conexion 
conexion = sqlite3.connect("sqlite3/test.sqlite3")

#seleccionar el cursor para iniciar la consulta
consulta = conexion. cursor()

#Valor de los argumentos 
argumentos = (cadena_texto, entero, decimal, datetime.date.today()) 

#vamos a crear un string con la consulta SQL 
sql = """
INSERT INTO test(cadena_texto,entero,decimal, fecha)
VALUES (?, ?, ?, ?)
""" 

#Realizar la consulta
if(consulta.execute(sql, argumentos)): 
    print("Registro guardado con exito")
else: print("ha ocurrido un error al guardar el registro")

#terminamos la consulta
consulta.close()
#guardamos los cambios en la base de datos
conexion.commit()
#cerramos conexion
conexion.close()