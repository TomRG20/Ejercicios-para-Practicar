"""
Autor: Tomás Rodríguez Garrido
Fecha: 09/05/2022
Probaremos las funciones lambda con otras estructuras

"""

#funciones SUMA, RESTA, MULTIPLICACIÓN, DIVISIÓN

print("\nSuma de dos números ")
num1 = 4
num2 = 9

suma = lambda num1, num2: num1 + num2
print(suma(num1, num2))

print("\nResta de dos números ")
num1 = 14
num2 = 9

resta = lambda num1, num2: num1-num2
print(resta(num1, num2))

print("\nMultiplicación de dos números ")
num1 = 14
num2 = 19

multiplicacion = lambda num1, num2: num1*num2
print(multiplicacion(num1, num2))

print("\nDivisión de dos números ")
num1 = 74
num2 = 9

divi = lambda num1, num2: num1/num2
print(divi(num1, num2))

# a partir de aquí usaremos alguna estructura.

miSet1 = {10, 34, 20, 12, 5, 34, 23, 1}
num3 = 50
print("Mi set original: ", miSet1)

anyadir = lambda miSet1, num3: {miSet1.add(num3)}
anyadir(miSet1, num3)  # llamada a la funcion
print("Mi set después de añadir 1 elemento:", miSet1)

# Caso para que me salga un "error" ya que no esta en el set el num3
num3 = 26
elim = lambda miSet1, num3: miSet1.remove(num3) if(num3 in miSet1) else print(num3, "No está en el set")
elim(miSet1,num3)
# caso bueno
num3 =50
elim = lambda miSet1, num3: miSet1.remove(num3) if(num3 in miSet1) else print(num3, "No está en el set")
elim(miSet1,num3)
print("Mi set después de eliminar con remove:", miSet1)

# El discard me elimina el elemento si lo encuentra, sino no hace nada,por lo que no hace falta el if
num3 = 12
elim = lambda miSet1, num3: miSet1.discard(num3)
elim(miSet1, num3)
print("Mi set después de eliminar con discard:", miSet1)

# Usaremos la funcion POP para eliminar un elemento aleatorio
popi = lambda miSet1: miSet1.pop()
popi(miSet1)
print("Mi set después de hacerle un POP:", miSet1)

# voy a añadir 3 elementos más y luego eliminaremos siempre el ULTIMO del set
miSet1.add(54)
miSet1.add(78)
miSet1.add(3)
print("Mi set después de añadir 3 elementos más:", miSet1)

miSet2 = set() #set auxiliar, así se crean los set vacios

tam = len(miSet1) #esto me dira el tamaño total del set
conta = 0 #contador auxiliar

for x in miSet1: 
    if conta < tam-1:
        miSet2.add(x)
    conta +=1 #incremento el contador

miSet1 = miSet2
print("Mi set después de eliminar el último:", miSet1)

# Ahora nos quedaremos solo los impares de ese set  /// filter(parametro condicion, parametro iterable)
miSet2 = set(filter(lambda x: x % 2 != 0, miSet1))
print("Los impares de mi set son: ", miSet2)  # me imprime 3,5 que son los impares
print(miSet1)  # me sigue imprimiendo mi set normal

