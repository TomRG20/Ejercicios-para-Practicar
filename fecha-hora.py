#trabajar horas y fechas
from datetime import date, datetime

#-------------------------------------------OBJETO DATE-------------------------------------------

print("Fecha actual: ", date.today()) 
print("Dia del mes: ", date.today().day)
print("Mes del año: ", date.today().month) #nos devuelve un digito del 1 al 12
print("Año: ", date.today().year)
print("Día de la semana: ", date.today().weekday()) #nos devuelve un digito del 0 al 6

#Diccionarios para las fechas personalizadas
mes = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto",
 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
dia_semana ={0:"Lunes", 1:"Martes", 2:"Miercoles", 3:"Jueves", 4:"Viernes", 5:"Sabado", 6:"Domingo"}

fecha = "Hoy " +dia_semana[date.today().weekday()] + " " + str(date.today().day)+ " de "
 + mes[date.today().month] + " del " + str(date.today().year)
print("Fecha actual: ", fecha)  #devuelve: Hoy Lunes 8 de Julio del 2019


#------------------------------------------OBJETO DATETIME-----------------------------------------

print("\n\nFecha y hora actual: ", datetime.now())
print("Segundos actuales: ", datetime.now().second)
print("Minutos actuales: ", datetime.now().minute)
print("Hora actual: ", datetime.now().hour)
print("Microsegundos actuales: ", datetime.now().microsecond)

#DIRECTIVAS personalizadas: strftime(string) 
#Fecha
# %Y: año con 4 digitos
# %m: mes con dos digitos
# %d: dia con dos digitos

#Hora
# %H: Hora con formato 24 horas y dos digitos
# %M: Minutos actuales con dos digitos
# %S: Segundos actuales con dos dígitos

print(datetime.now().strftime("%d-%m-%Y  %H:%M:%S"))  #devuelve 08-07-2019  23:38:53

#podemos usar solo el datetime en vez del time: 
print("El día del mes: ", datetime.today().day)
print("El mes del año: ", datetime.today().month)
print("Año: ", datetime.today().year)
#---------------------------------------------------------------------------------------------------