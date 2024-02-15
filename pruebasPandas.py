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

print("\nLeer un fichero csv ----------------")
dffichero = pd.read_csv("speedTest.csv", sep="[,:|]", engine="python")
print(dffichero)

#conseguiremos filas a partir de indices de tipo string
print("\nAtributo loc ----------------")
d2 = pd.DataFrame(diEmpleados)
#creo indices a mi gusto
d2 = pd.DataFrame(diEmpleados, index=['a','b','c','d','e'])

print('\n', d2)

print('\n', d2.loc['a'])

print('\n', d2.loc['b':'d'])

print('\n', d2.loc['b':'d', ['nombre','puesto']])

#  int   -  String
#  iLoc  -   Loc

print("\nAtributo iLoc ----------------")
d3 = pd.DataFrame(diEmpleados, index=[0,1,2,3,4])

print('\n', d3)

print('\n', d3.iloc[1])

print('\n', d3.iloc[1:4])

print('\n', d3.iloc[1:4, [0,2]])
print('\n', d3.iloc[1:4] [['nombre','email','puesto']])

print("\nCondicionales ----------------")
d4 = pd.DataFrame(diEmpleados, index=[0,1,2,3,4])
print('\n', d4)
print('\n', d4[(d4['puesto']=='Contable')])
print('\n', d4[(d4['puesto']=='Contable')]['nombre'])

print('\n', d4[(d4['envacaciones']==True)])
print('\n', d4[(d4['envacaciones']==True)]['nombre'])

# or = | 
# and = & 


print("\nOrdenamiento ----------------")
dOrdenado = pd.read_csv("speedTest.csv", sep="[,:|]", engine="python")
print(dOrdenado)

#las 5 descargas más lentas
print('\n', dOrdenado.sort_values(by='Downspeed').head(5))

#las 3 subidas más rápidas
print('\n', dOrdenado.sort_values(by='Upspeed').tail(3))
print('\n', dOrdenado.sort_values(by='Upspeed', ascending=False).head(3))

print("\nBusqueda por rangos ----------------")
dOrdenado2 = pd.read_csv("speedTest.csv", sep="[,:|]", engine="python")
print(dOrdenado2)

print(dOrdenado2[ (dOrdenado2['Downspeed'] >= 240) & (dOrdenado['Downspeed'] <= 260) ])
print(dOrdenado2[ dOrdenado2["Downspeed"].between(240, 260)])

print(dOrdenado2[ (dOrdenado2["Downspeed"].between(240, 260)) & (dOrdenado2["Upspeed"].between(130, 140))])


print("\nBusqueda entre opciones ----------------")
d4 = pd.DataFrame(diEmpleados, index=[0,1,2,3,4])
print('\n', d4)


puesto = ["Abogada","Jefe de departamento","Contable"]
print('\n', d4[(d4['puesto'].isin(puesto))])

print('\n', d4[(d4['envacaciones']==True) & (d4['puesto'].isin(puesto))])


print("\nMétodos de strings ----------------")
d4 = pd.DataFrame(diEmpleados, index=[0,1,2,3,4])
print('\n', d4)
print('\n', d4[d4['puesto'].str.startswith('A')])

print('\n', d4[d4['nombre'].str.contains('a')])

print('\n', d4[d4['nombre'].str.endswith('a')])


print("\nAgrupación ----------------")
d4 = pd.DataFrame(diEmpleados, index=[0,1,2,3,4])
print('\n', d4)

print('\n', d4.groupby('envacaciones')['envacaciones'].count())
