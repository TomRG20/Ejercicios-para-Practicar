"""
    Prueba inicial de un código Python para configurar el Conector MySQL en su
    sistema e Insertar los datos en la Tabla MySQL,
    después de lo cual se obtienen y muestran los datos de la Tabla.
    
"""
import mysql.connector               # pip install mysql-connector-python


#abro una primera conexion para crear la Base de datos
mydb = mysql.connector.connect (
    host ="localhost",
    user ="root",
    password =""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE myDB") # creo MyDB 
mydb.close() #cierro la conexión

#Abro una nueva conexion ya indicando en que base de datos trabajaré
mydb2 = mysql.connector.connect (
    host ="localhost",
    user ="root",
    password ="",
    database="myDB"  # mi base de datos
)

mycursor2 = mydb2.cursor()

mycursor2.execute("CREATE TABLE human (names VARCHAR(255), surName VARCHAR(255))") # create the MySQL DataTable

mycursor2.execute("SHOW TABLES")
for x in mycursor2:
    print(x)
    
#Ahora tengo que insertar 1 tupla de datos 
sql = "INSERT INTO human (names, surName) VALUES (%s, %s)"
val = ("Paco", "Ramirez")
mycursor2.execute(sql, val)
mydb2.commit() #es requerido para hacer cambios
print(" ", mycursor2.rowcount, " Tupla Insertada...", end="\n")

#Ahora insertaremos varias tuplas a la vez
val2 = [
  ('Pedro', 'Fernández'),
  ('Ana', 'Palacios'),
  ('Gonzalo', 'Ruiz'),
  ('Miguel', 'Velasco'),
  ('Sandra', 'Moreno'),
  ('Beatriz', 'García'),
  ('Rafael', 'Muñoz')
]

mycursor2.executemany(sql, val2)
mydb2.commit()
print(" ", mycursor2.rowcount, " Tuplas Insertadas...", end="\n")

#Ahora tendría que mostar los datos de la tabla
mycursor2.execute("SHOW TABLES")
for t in mycursor2:
    print("\n\nTabla: ", t, end="\n")
    print("--------------------", end="\n")

mycursor2.execute("SELECT * FROM human")
myresult = mycursor2.fetchall()

for x in myresult:
    print(x)

mydb2.close() #cierra la conexion con la BD