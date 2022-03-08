"""
Programa: Ejercicio 3, calcular la Media de 5 números
Version: 1.0
Autor: Tomás Rodríguez
Fecha: 21 de diciembre de 2020

"""
# dado 5 números enteros  ------------------------------------------------------------------------------------------
n1,n2,n3,n4,n5 = 20,30,23,56,78
n_num = 5

suma_Numeros = n1 + n2 + n3 + n4 + n5
media = suma_Numeros / n_num

print("La Media entera de los números es: %d" %media)
print("La Media real de los números es: %2.1f" %media)  #esto es solo para que veas la diferencia entre real y entero

# Solicitando los 5 números por consola  ----------------------------------------------------------------------------
n1 = float(input("Introduce el primer numero: "))
n2 = float(input("Introduce el segundo numero: "))
n3 = float(input("Introduce el tercer numero: "))
n4 = float(input("Introduce el cuarto numero: "))
n5 = float(input("Introduce el quinto numero: "))

suma_Numeros = n1 + n2 + n3 + n4 + n5
media = suma_Numeros / n_num

print("La Media entera de los números es: %d" %media)
print("La Media real de los números es: %2.1f" %media)  #esto es solo para que veas la diferencia entre real y entero

