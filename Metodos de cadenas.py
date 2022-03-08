"""
Programa: Programa Ejemplo sobre la manipulación de cadenas y los *** Métodos de las cadenas ***
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 30 de diciembre de 2020

"""
# Cadenas para probar: 
cadena_de_pruebas = "hola Mundo! esto solo es una cadena de prueba, para ver los diferentes métodos o funciones de las cadenas "
cadena_test = "-Hola-Alfonso!-¿Qué-tal-estas?-" 
cadena_test_num = "123"
cadena_test_dig = "ABCDabdc"
################################################################################################################################

# CONCATENAR CADENAS: 
res = "Hola" + " " + " y adios"
print(res) 

m1 = "Hola"
m2 = " y adios 2"
res = m1 + m2
print(res)

# MULTIPLICAR CADENAS:
res = "Hola " * 3
print(res)  # Me imprimirá una cadena "hola" repetida en este caso 3 veces. 

# AÑADIR CADENAS:
res = "Hola"
res += " "
res += m2
print(res, " \n\n" )


# METODOS DE CADENAS: 
res = cadena_de_pruebas.capitalize() # pone la primera letra de la cadena en mayuscula
print(res)
res = cadena_de_pruebas.upper() # pone todo el texto en mayuscula
print(res)
res = cadena_de_pruebas.lower() # pone todo el texto en minuscula
print(res)
res = cadena_de_pruebas.strip() # devuelve la cadena sin el espacio inicial ni final (si lo tuviera)
print(res)
res = cadena_de_pruebas.swapcase() # devuelve la cadena con las mayusculas pasadas a minus y viceversa
print(res)
res = cadena_de_pruebas.title() # devuelve la cadena con formato titulo, es parecido a capitalize
print(res)
res = cadena_de_pruebas.replace("d", "J") # si necesitas reemplazar una cadena por otra(lo hace tantas veces como d existan)
print(res)

res = len(cadena_de_pruebas) # cuenta el número de caracteres de la cadena, los espacios en blanco tambien. 
print("El tamaño de la cadena es: ", res)

res = cadena_de_pruebas.count("de") # cuenta los "de" que hay dentro de la cadena y nos devuelve un entero
print("El número de \"de\" es de: ", res)

# Busca una subcadena (solo 1 vez), dentro de la cadena y te indicará el indice del inicio de está, sino esta devuelve -1
res = cadena_de_pruebas.find("para")  
print("La subcadena empieza en: ", res)

res = cadena_test.strip() # devuelve la cadena sin el espacio inicial ni final (si lo tuviera)
print(res)
res = cadena_test.strip("-") # tambien podemos usar este metodo para eliminar un caracter al inicio y final
print(res)
res = cadena_test.split("-") # el split podemos usarlo para separar una cadena y crear una lista con cada elemento
print(res)
res = cadena_test.startswith("-Hola") # devuelve True si la cadena empieza con la subcadena "-hola" en este caso
print(res)
res = cadena_test.endswith("?-") # devuelve True si la cadena finaliza con la subcadena "-hola" en este caso
print(res)

res = cadena_test.isalnum() # devuelve True si la cadena es todo números o carácteres alfabéticos, sino False
print(res)
res = cadena_test_dig.isalpha() # devuelve True si la cadena es todo caracteres alfabéticos
print(res)
res = cadena_test_num.isdigit() # devuelve True si la cadena es todo números, sino False
print(res)
res = cadena_test.islower() # devuelve True si la cadena es todo minúsculas
print(res)
res = cadena_test.isupper() # devuelve True si la cadena es todo mayusculas 
print(res)
res = cadena_test.isspace() # devuelve True si la cadena es todo espacios en blanco
print(res)
res = cadena_test.istitle() # devuelve True si la primera letra de cada palabra es mayuscula 
print(res)