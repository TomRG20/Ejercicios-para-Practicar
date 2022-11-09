"""
Esto solo vale para hacer pruebas
"""

import statistics as st

# las notas de un examen cualquiera
notas = [7, 5, 3, 5, 10, 9, 8, 2, 1, 1, 4, 5, 6, 6, 8, 7]

print(f"La media aritmetica es: {st.mean(notas)}")
print(f"La mediana es: {st.median(notas)}")
print(f"La moda es: {st.mode(notas)}")
print(f"La desviación estándar es: {st.stdev(notas)}")
print(f"La varianza poblacional es: {st.pstdev(notas)}")
print(f"La varianza es: {st.variance(notas)}")
print(f"La p-varianza es: {st.pvariance(notas)}")


"""
import math as m

print(f"El número PI es: {m.pi}")  # constantes
print(f"El número e es: {m.e}")

print(f"EL seno de 40 es: {m.sin(40)}")  # funciones trigonometricas
print(f"El coseno de 60 es: {m.cos(60)}")
print(f"Raiz cuadrada de 50: {m.sqrt(50)}")
print(f"De radianes a grados sexagesimales: {m.radians(30)}")
print(f"De grados sexagesimales a radianes : {m.degrees(0.5)}")

print(f"Devuelve e elevado a 2: {m.exp(2)}")  # funciones potencia y logaritmicas
print(f"Logaritmo en base 2 de 6: {m.log2(6)}")
print(f"Logaritmo en base 10 de 6: {m.log10(6)}")
print(f"Devuelve 2 elevado a 2: {m.pow(2,2)}")

print(f"Redondea al mayor: {m.ceil(5.67)}")  # funciones numericas
print(f"Redondea al menor: {m.floor(5.67)}")
print(f"Devuelve el MCD: {m.gcd(6,21)}")

"""




















"""
# Ejemplo de la nueva implementacion del Switch case con match case

lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

"""




