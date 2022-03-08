#Esta funcion tiene valores por defecto, para que nunca esten en blanco
#con esto podemos conseguir hacer llamadas con 1 solo parametro

def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)

# call the function here
introduction("James", "Doe") #Machaca Smith y poner Doe
introduction("James")        #Si pongo solo 1 parametro coge por defecto Smith
introduction(firstName="William") #igual que la anterior

def introduction(firstName="John", lastName="Smith"):
    print("Hello 2, my name is", firstName, lastName)

# call the function here
introduction() #me imprime John Smith
introduction(lastName="Hopkins")

