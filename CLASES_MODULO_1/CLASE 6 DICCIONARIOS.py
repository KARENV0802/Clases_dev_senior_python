ConceptosProgramacion = {
    'POO': 'Programación orientada a objetos',
    'IDE': 'Entorno de desarrollo integrado',
    'DBMS': 'Sistema de gestión de bases de datos',

}

print (ConceptosProgramacion)
print (len(ConceptosProgramacion)) #Para saber cuantos elementos tiene el diccionario

print(ConceptosProgramacion['IDE']) #Para imprimir un solo elemento del diccionario
print(ConceptosProgramacion.get('POO')) #Para imprimir un solo elemento del diccionario

ConceptosProgramacion ['DBMS'] = 'Database Management System' #Para modificar un elemento del diccionario

for keys in ConceptosProgramacion:
    print (keys) #Para recorrer el diccionario

for key, value in ConceptosProgramacion.items():
    print (key, value) #Para recorrer el diccionario

