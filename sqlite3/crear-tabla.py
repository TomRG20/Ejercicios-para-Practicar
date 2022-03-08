import sqlite3

#conectar a la base de datos
conexion = sqlite3.connect("sqlite3/test.sqlite3")

#seleccionar el cursor para realizar la consulta
consulta= conexion.cursor()

sql = """
CREATE TABLE IF NOT EXISTS test(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
cadena_texto VARCHAR(50) NOT NULL,
entero INTEGER NOT NULL,
decimal FLOAT NOT NULL,
fecha DATE NOT NULL)"""

#ejecutar la consulta
if(consulta.execute(sql)): 
    print("Tabla creada con exito")
else: print("Ha ocurrido un error al crear la tabla")

#terminamos la consulta
consulta.close()

#guardamos los cambios en la base de datos
conexion.commit()

#cerramos conexion a base de datos
conexion.close()
