myList = [1, 2, 4, 4, 1, 4, 2,8, 6, 2, 9]
#
# put your code here
#
newList = [] #lista auxiliar

for i in range(0, len(myList)):
    if(myList[i] not in newList): #sino esta en la auxiliar lo añade
        newList.append(myList[i])
        continue

myList = newList #machacamos la anterior por la auxiliar
myList.sort() #ordena la lista
print("The list with unique elements only:")
print(myList)