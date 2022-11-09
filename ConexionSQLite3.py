import  sqlite3

#creamos la conexion a la BD..
conex = sqlite3.connect("Alumnos.db")

#creamos un cursor para hacer opera..
con = conex.cursor()

#creamos una tabla
con.execute(""" CREATE TABLE estudiante(
    matricula TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    notaMedia REAL) """)

#inserto en la base de datos
con.execute("INSERT INTO estudiante VALUES('01','Pedro','Ruiz', 5.2)")

#actualizo la base de datos
conex.commit()

#imprimo todos los estudiantes
con.execute("SELECT * FROM estudiante")
estudiantes = con.fetchall()
print(estudiantes)

#cerrar conexion a la BD
conex.close()