'''
Ejercicio.
Pedir una lista de 10 números introducidos por teclado, ordenarlos y mostrarlos por pantalla
Perdir una lista de 10 nombres introducidos por teclado, ordenarlos y mostrarlos por pantalla
'''

#crear una lista
miLista=[] #lista de números
miLista2=[] #lista alfanumerica

for i in range(10):
    #pedir número
    num= int(input("Introduce el "+ str(i+1) +"º número: "))
    #añadir elemento a la lista    
    miLista.append(num)
    
#imprimir lista    
print("\n\tMi lista Original: ",miLista, end="\n")

#ordenar lista con sort
miLista.sort()
print("\n\tMi lista Ordenada: ",miLista, end="\n")

#invertir la lista con sort reverse
miLista.sort(reverse= True)
print("\n\tMi lista Alreves: ",miLista, end="\n\n")

 


for i in range(10):
    #pedir nombre
    nombre= input("Introduce el "+ str(i+1) +"º nombre: ")
    #añadir elemento a la lista    
    miLista2.append(nombre)

#imprimir lista
print("\n\tMi lista de nombres original: ",miLista2, end="\n")
#ordenar lista con sort

miLista2 = sorted(miLista2)
print("\n\tMi lista de nombres ordenada: ",miLista2, end="\n")

miLista2.reverse()
print("\n\tMi lista de nombres Alreves: ",miLista2, end="\n\n")