year = int(input("Enter a year: "))

# COMO SACAR SI ES BISIESTO O NO UN AÑO: 
# El calendario gregoriano tiene años bisiestos cada 4 años bajo
# la siguiente regla: serán bisiestos los años múltiplos de 4, 
# exceptuando los múltiplos de 100, salvo los que sean múltiplos de 400.
#
# EL GREGORIANO FUE IMPUESTO EN 1582. toda cifra menor saldra un aviso.

if(year >= 1580):
    if( year % 4 != 0): print("it's a common year")
    elif(year % 100 != 0): print("it's a leap year") #año bisiesto
    elif(year % 400 != 0): print("it's a common year")
    else: print("it's a leap year") #año bisiesto
else:
    print("Not within the Gregorian calendar period") #este aviso


tup = (1, ) + (1,)
tup = tup + tup
print(len(tup))
