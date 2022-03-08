########### Las funciones integradas: ############

#  divmod()   devuelve una tupla formada por el 
#cociente y el resto de la division entre 2 numeros
#------------ divmod(13,4) ---------------
#------------ devuelve -> (3,1) ----------

#  pow()      permite calcular potencias o raices
#Si se le pone un tercer argumento, la funcion calcula 
#primero x elevaado a y, después calcula el resto de la
#division por z        pow(x,y,z)
#------------ pow(2,3) --------------
#------------ devuelve -> 8 ---------
#------------ pow(2,3,5) ------------
#------------ devuelve -> 3 ---------

#  round()  permite redondear una cifra
#Permite 1 o 2 argumentos
#------------- round(4.35) -> devuelve 4 ----------
#------------- round(4.3527, 1) -> devuelve 4.4 ---
#------------- round(4.45, 1) -> devuelve 4.5 ----- 
#------------- round(0.315,2) -> devuelve 0.32 ----

# floor() y ceil()  redondear al entero anterior o posterior
#Incluidas en la biblioteca math. 
#------------- from math import floor -----------
#------------- floor(5/2) -> devuelve 2 ---------
#------------- floor(2.9999) -> devuelve 2 ------
#------------- ceil(5/2) -> devuelve 3 ----------
#------------- ceil(2.0001) -> devuelve 3 -------

# abs() valor absoluto 
#calcula el valor absoluto de un numero, es decir, el valor sin signo
#------------- abs(-6) -> devuelve 6 ------------

#  max() máximo valor
#La funcion calcula el valor máximo de un conjunto de valores
#En el caso de cadenas, el valor máximo corresponde al valor alfabético
#-------------- max(4, 5, -2, 9, 3.5, -10) -> devuelve 9 --------------
#-------------- max("David", "Alicia", "Tomás") -> devuelve 'Tomás' ---

#  min() mínimo valor
#La funcion calcula el valor mínimo de un conjunto de valores
#En el caso de cadenas, el mínimo corresponde al valor alfabético 
#-------------- min(3, 4, -2, 5, -10) -> devuelve -10 -----------
#-------------- min("David", "Alicia") -> devuelve 'Alicia' -----

#  sum() suma de un conjunto de números
#-------------- sum(range(6)) -> devuelve 15 
#-------------- sum((1,2,3,4,5)) -> devuelve 15

# sorted()  Ordenación de una tupla, rango, lista, conjunto o diccionario
#--- sorted((10,2,9,-3,6)) -> devuelve [-3, 2, 6, 9, 10] 
#--- sorted(("David","Alicia",Tomás","Emilio")) -> ['Alicia', 'David', 'Emilio', 'Tomás']

# import math 

# math.sqrt(x) devuelve la raíz cuadrada de un número.
# math.log(x) calcula el logaritmo natural (o neperiano) de un número.
# math.exp(x) calcula la exponencial de un número.

# math.sin(x) para el seno.
# math.cos(x) para el coseno.
# math.tan(x) para la tangente. 
# math.acos(x) para el arco coseno.
# math.asin(x) para el arco seno
# math.atan(x) para la arco tangente.

# math.degrees(x) calcula los grados que equivalen a una cierta cantidad de radianes,
# math.radians(x) convierte a radianes una cierta cantidad de grados.

# También tenemos alguna constante que nos puede simplificar la vida: 
# math.pi representa el número "PI".
# math.e representa el número "e".