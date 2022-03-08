# Fibonacci numbers
# Rules: 
#    the first element of the sequence is equal to one (Fib1 = 1)
#    the second is also equal to one (Fib2 = 1)
#    every subsequent number is the sum of the two preceding numbers (Fibi = Fibi-1 + Fibi-2)

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # testing
    print(n, "->", fib(n))

