import numpy as np

a = np.array([10, 17, 20, 25, 29, 30])
print(a[a % 2 != 0], end="\n")


# array de 2 dimensiones (matrices)
b = np.array([[1, 2, 3], [4, 5, 6]]) 
print(b[1,2], end="\n") 

c = np.zeros(3)  # me devuelve una lista de 3 ceros
print(c, end="\n")

d = np.eye(8)  # me devuelve una matriz identidad (8x8)
print(d, end="\n")

e = np.ones(6)
print(e, end="\n")

f = np.full(3, 5)
print(f, end="\n")

g = np.identity(6)
print(g, end="\n")

h = np.arange(1, 10, 2)
print(h, end="\n")

i = np.linspace(0, 10)
print(i, end="\n")

j = np.random.randn(5)
print(j, end="\n")

k = np.random.randint(5)
print(k, end="\n")

l = np.random.rand(5)
print(l, end="\n")

m = np.random.random(5)
print(m, end="\n")


