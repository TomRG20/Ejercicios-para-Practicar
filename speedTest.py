'''
Programa:Programa para medir la velocidad de internet usando la libreria speedtest
        guardando los datos en un fichero csv, luego leyendo tal fichero csv y con 
        la libreria matplotlib mostraremos una gráfica con los diferentes valores 
        de velocidad de subida y bajada de nuestro internet y un promedio de ambos.
Autor: Tomás Rodríguez
Version:1.0
Fecha: 11/07/23
'''

import speedtest as spt
import datetime
import csv
import matplotlib.pyplot as plt
import numpy as np

test = spt.Speedtest(secure=True)

t = []
down = []
up = []


with open('speedTest.csv', mode='w', newline='') as spv:
    csv_writer = csv.DictWriter(spv, fieldnames=['Time','Downspeed','Upspeed', 'Ping'])
    csv_writer.writeheader()

    nPruebas = 10
    prueba = 0

    #print(f"Cliente: {test.results.client}")
    cliente = test.results.client
    print(f"IP: {cliente.get('ip')}")
    print(f"Lat: {cliente.get('lat')}")
    print(f"lon: {cliente.get('lon')}")
    print(f"Isp: {cliente.get('isp')}")
    print(f"Pais: {cliente.get('country')}")


    while(prueba < nPruebas):
        print(f"Prueba número: {prueba + 1}/10 ", end=" ")
        time = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed = round((round(test.download()) / 1048576), 2)
        upspeed = round((round(test.upload()) / 1048576), 2)
        ping = test.results.ping
        print(f"time: {time}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s, Ping: {ping} ms")
        
        csv_writer.writerow({
            "Time": time,
            "Downspeed": downspeed, 
            "Upspeed": upspeed,
            "Ping": ping
        })

        prueba += 1
        spv.flush()

        
with open('speedTest.csv', newline='') as spv:
    csv_reader = csv.DictReader(spv)
    for row in csv_reader:
        #print(row['Time'], row['Downspeed'])
        t.append(row['Time']) 
        down.append(row['Downspeed'])
        up.append(row['Upspeed'])

    spv.flush()


#now we can drow the grafic 
down =[float(d) for d in down]
medDown = round(sum(down) / len(down) , 2)
up = [float(u) for u in up]
medUp = round(sum(up) / len(up) , 2)

plt.plot(t, down, marker='*', label = 'Avarage Down '+ str(medDown) +' Mb/s', color='navy', linestyle="--")
plt.plot(t, up, marker='o', label = 'Avarage UP ' + str(medUp) + ' Mb/s', color='green', linestyle="--" )

for i, label in enumerate(down):
    plt.annotate(label, (t[i], down[i]), ha='center', va='bottom',color='seagreen')
for i, label in enumerate(up):
    plt.annotate(label, (t[i], up[i]), ha='center', va='bottom',color='teal')

plt.xlabel("Tiempo", color='slategray')
plt.ylabel("Velocidad Internet", color='slategray')
plt.legend()
plt.savefig('speedTest.jpg', bbox_inches= 'tight')
plt.title('Internet - Speed Test', color='slategray')
plt.show()