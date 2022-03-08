import sqlite3

conexion = sqlite3.connect("sqlite3/test.sqlite3")
consulta = conexion.cursor()

#Extrayendo todas las filas
sql = "SELECT * FROM test"

if(consulta.execute(sql)):
    filas = consulta.fetchall()
    for fila in filas:
        print(fila[0], fila[1], fila[2], fila[3], fila[4])
    
#Extrayendo una sola fila con id = 2
sql = "SELECT * FROM test WHERE id = %s" % 2 
consulta.execute(sql)
fila = consulta.fetchone()
print("\nSeleccionando un solo registro con id 2: ", fila[0], fila[1], fila[2], fila[3], fila[4])   
   
argumentos = (1, 2)
#Extrayendo entre un rango con BETWEEN
sql = "SELECT * FROM test WHERE id BETWEEN ? AND ?"
consulta.execute(sql, argumentos)
filas = consulta.fetchall()

print("\nMostrando filas con BETWEEN 1 y 2: \n")
for fila in filas:
    print(" ", fila[0], fila[1], fila[2], fila[3], fila[4])  #de forma indexada

consulta.close()
conexion.commit()
conexion.close()