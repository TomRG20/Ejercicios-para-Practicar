
income = float(input("Enter the annual income: "))

#Tome medio, a partir del cual se mide de una y otra forma la tax
incomeTop = 85528  

if income < incomeTop:  tax = ((income * 18)/100) - 556.02 
else: 
    if income > incomeTop: 
        surplus = income - 85528
        tax = 14839.02 + ((surplus * 32)/100)
 
#Si los impuestos son menores de 0 valen 0       
if tax <0: tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")