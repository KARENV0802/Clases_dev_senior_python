paises = ('colombia', 'mexico', 'ecuador', 'venezuela')

#Todos los mismos comandos de las listas se pueden aplicar a las tuplas
print (paises) #Para imprimir la tupla
print (type(paises)) #Para saber que coleccion estoy imprimiendo
print (len(paises)) #Para saber cuantos elementos tiene la tupla
print (paises[0]) #Para imprimir un solo elemento de la tupla
print (paises[-1]) #Para saber cual es el ultimo elemento de la tupla
print (paises.index('mexico')) #Para saber en que posicion esta un elemento de la tupla
print (paises.count('colombia')) #Para saber cuantas veces se repite un elemento en la tupla

for pais in paises:
    print (pais) #Para recorrer la tupla

#Para convertir una tupla en una lista
paises_lista = list(paises)
paises_lista[1] = 'Argentina'
paises = tuple(paises_lista) #Para convertir una lista en una tupla
print (paises) #Para imprimir la tupla

del paises #Para eliminar una tupla
