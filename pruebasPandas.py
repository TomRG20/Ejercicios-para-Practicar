import pandas as pd
import numpy as np

#series
colores = pd.Series(["blanco","amarillo","verde","azul"])
print(type(colores)) # pandas series es un objeto de tipo serie 
print(colores) # me muestra los indices y los valores de la serie y su tipo object

print("\nAtributos -----------------------------")
print(colores.size)
print(colores.dtype)
print(colores.shape)
print(colores.index)

print("\nSeries a partir de diccionarios -------")
diColores={"blanco": 100, "amarillo": 200, "verde": 300, 'azul': 400}
colores2 = pd.Series(diColores) # creo una nueva serie a partir de un diccionario
print(type(diColores))
print(diColores)

print("\nAtributos -----------------------------")
print(colores2.size)
print(colores2.dtype)
print(colores2.shape)
print(colores2.index)

#valores nulos
print(np.nan)
nulo = pd.Series([1, 3, 5, np.nan, 9, np.nan, 15])
print(nulo.isnull())



#dataframe
print("\nDataFrame a partir de diccionarios -------")
diEmpleados={"nombre": ["Pepe", "Maria", "Juan", "Manolo", "Javier"],
             "email": ["pepe@example.com", "maria@example.com","juan@example.com","manolo@example.com","javier@example.com"], 
             "puesto": ["Administrativo", "Abogada", "Recursos Humanos", "Contable", "Jefe de departamento" ],
             "envacaciones": [True,False,False,True,False]
            }
d=pd.DataFrame(diEmpleados) 
print(d)

print("\nAtributos -----------------------------")
print(d.size)
print(d.dtypes)
print(d.shape)
print(d.index)

print("\nValores de una columna ----------------")
print(d["nombre"]) 

print("\nValores de una columna y fila ---------")
print(d["nombre"][1]) 

print("\nCrear una nueva serie para agregarla como columna a nuestro dataframe ---------")
anyoExperiencia = pd.Series([2,5,3,6,12])

d['experiencia'] = anyoExperiencia   #agregamos la nueva serie al dataframe
print(d)

#renombrar las columnas, esto genera un nuevo dataframe, pero el original sigue igual
e = d.rename(
    columns = {"envacaciones":'vacaciones'}
)
print(e) 
#si quisieramos que ese dataframe original se modificara directamente tenemos que asignarlo
d = d.rename(
    columns = {"envacaciones":"vacaciones"}
)
print(d)

print("\nEliminar una columna ----------------")
del d["experiencia"]
print(d)

dffichero = pd.read_csv("fichero.csv", sep="[,;:|_]", engine="python")


