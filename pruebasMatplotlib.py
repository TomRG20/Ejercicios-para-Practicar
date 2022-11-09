import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


x = np.linspace(0, 30, 200)
y = np.exp(-0.1*x)*np.cos(x)
plt.plot(x, y, "m")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (mm)")
plt.title("Gráfica de posición")
plt.text(10, 0.5, "Algo informativo", fontsize=16, color="r", 
         name="Times New Roman")
plt.show()


x = np.linspace(0, 2*np.pi, 1000)
a,k,phi0 = 3,9,10
r = a*np.cos(k*x + phi0)
plt.polar(x, r, "g")
plt.show() 


manzanas = [30,5,23,27]
nombres = ["Pepe","Juan","Dario","Cristian"]
colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
desfase = (0, 0, 0, 0.1)
plt.pie(manzanas, labels=nombres, autopct="%0.1f %%", colors=colores, explode=desfase);
plt.axis("equal")
plt.show() 






"""
Grafica valor del gas 2022

plt.plot(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre"], 
[7.346, 5.572, 5.832, 8.065, 9.401, 9.664, 9.413, 10.005, 9.372], 'r--o', label="Precio del Gas")
plt.ylabel("Dolares ($)")
plt.xlabel("Meses")
plt.title("Precios Maximos del gas en 2022")
plt.text(4,8,"$ Valores en USD $", color="b")
plt.legend()
plt.grid(ls="--", color="#dadada")
plt.show() 
"""