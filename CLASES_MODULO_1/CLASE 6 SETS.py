lenguajes = {'Java', 'Python', 'JavaScript'}

print(lenguajes)
print(len(lenguajes)) #Para saber cuantos elementos tiene el set
print('go' in lenguajes) #Para saber si un elemento esta en el set  
lenguajes.add('Go') #Para agregar un elemento al set
print(lenguajes)

for lenguaje in lenguajes:
    print(lenguaje) #Para recorrer el set uno debajo del otro

lenguajes.remove('Go') #Para eliminar un elemento del set

lenguajes.discard() #Para eliminar un elemento del set
