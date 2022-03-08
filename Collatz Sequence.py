print("Collatz Sequence\n")

c0 = int( input("Introduce un número entero mayor que 0: "))
steps = 0

while (c0 != 1):
    if (c0 % 2 == 0): 
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
    print("El valor es:", c0)

print("El número de pasos es:", steps) 
    