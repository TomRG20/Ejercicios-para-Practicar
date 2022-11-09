def cuentaAtras(num):
    #condicion
    if num > 0:
        #llamada recurrente
        print(num)
        num = cuentaAtras(num - 1)

#cuentaAtras(8)


def factorial(num):
    if num == 0 or num == 1: 
        return 1
    else: 
        if(num > 1): 
            return num * factorial(num - 1)


for n in range(-2, 10):  # testing
    print(f'El factorial del número {n} es: {factorial(n)}')

