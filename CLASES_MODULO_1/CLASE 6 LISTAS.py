nombres = ['juan', 'sebastian', 'melissa']

print (nombres)

#Para saber que coleccion estoy imprimiendo
print (type(nombres))

#para imprimir un solo elemento de la lista
print (nombres[0])

#Para saber cual es el ultimo elemento de la lista
print (nombres[-1])

#Para saber cuantos elementos tiene la lista
print (len(nombres))

#Para agregar un elemento a la lista
nombres.append('carlos')

#Para agregar un elemento en la posicion que queramos
nombres.insert(1, 'daniel')

#Para eliminar un elemento de la lista
nombres.remove('daniel')
nombres.pop() #Elimina el ultimo elemento de la lista
del nombres [0] #Elimina el elemento en la posicion que queramos

#Para saber si un elemento esta en la lista
nombres.index('sebastian') 

#para limpiar la lista
nombres.clear()

#Para eliminar una lista
del nombres

#Para copiar una lista
nombres = ['juan', 'sebastian', 'melissa']
nombres_copia = nombres.copy()

#Para unir dos listas
nombres2 = ['carlos', 'daniel']
nombres.extend(nombres2)

#Para contar cuantas veces se repite un elemento en la lista
nombres.count('juan')

#Para ordenar la lista
nombres.sort()

#Para invertir la lista
nombres.reverse() 





