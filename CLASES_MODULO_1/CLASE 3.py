age = 14
country = 'GER'
userHasDNI = True

# Primera condicion del codigo
if age >= 21:
    print('You can buy alcohol in USA')
# Si la primera condicion no es verdadera, se ejecutara la segunda condicion
elif age >= 18:
    print('You can buy alcohol in COL')
# si la condicion anterior no es verdadera, se ejecutara la siguiente condicion, puedes tener tanto elif como quieras
elif age >= 16:
    print('You can buy alcohol in GER')
# si todas las condiciones anteriores no son verdaderas, se ejecutará la ultima condicion
else:
    print('You can\'t buy alcohol')

# if condition:
# actions
if age >= 21 and country == "USA":
    print('You can buy alcohol in USA')
elif age >= 18 and country == "COL":
    print('You can buy alcohol in COL')
elif age >= 16 and country == "GER":
    print('You can buy alcohol in GER')
else:
    # userHasDNI = False
    print('You can\'t buy alcohol')

# para la variable en objectToIterate:
# acciones
# para cada valor de i en el rango de 10 (0-9)
# student = 0
# print(student)
# student = 1
# print(student)
# student = 2
# print(student)
# ...
# student = 9
# print(student)
for student in range(2):
    print(student)

# while condition:
#     actions

studentNumber = 0
while userHasDNI:
    studentNumber += 1
    print(studentNumber)
    if studentNumber == 10:
        userHasDNI = False

    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        userHasDNI = False
        print('You can\'t buy alcohol')

while userHasDNI:
    # block 1
    print("HELLO 1")
    
    # block 2
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
        # stop the block
        break
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        userHasDNI = False
        print('You can\'t buy alcohol')

    #block 3
    print("HELLO 2")

print("############## WHILE ##############")

# variable booleana para controlar el bucle en funcion de si el usuario tiene DNI
userHasDNI = True
while userHasDNI:
    # solicitar al usuario que ingrese su edad y pais
    age = int(input('Ingresa tu edad: '))
    country = input('Introduzca su pais: ')
    
    # block 1: Condiciones para determinar si el usuario puede comprar alcohol legalmente
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        #  Si no se cumple ninguna de las condiciones anteriores, el bucle se detiene
        userHasDNI = False
        print('You can\'t buy alcohol')

print("############## FOR ##############")

# Iteracion unica con un bucle for
for student in range(1):
    age = int(input('Ingresa tu edad: '))
    country = input('Introduzca su pais: ')
    
    # block 1: Las mismas condiciones de elegibilidad de alcohol que las anteriores
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        userHasDNI = False
        print('You can\'t buy alcohol')

print("############## WHILE 100 STUDENTS  NO DNI ##############")

# Inicializar contador para alumno sin DNI
studentsWithoutDNI = 0
while studentsWithoutDNI <= 3:
    age = int(input('Enter your age: '))
    country = input('Enter your country: ')
    
    # block 1: Consultar condiciones de elegibilidad para alcohol
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        # Si el usuario no puede comprar alcohol, incrementar el contador para estudiantes sin DNI 
        studentsWithoutDNI += 1 
        print('You can\'t buy alcohol')

print("############## FOR 10000 STUDENTS  SOLO ENCONTRAR 3 SIN DNI ##############")

# Reiniciar contador para alumnos sin DNI
studentsWithoutDNI = 0
for student in range(10000):  # Iterar sobre un rango amplio

    # Si hemos encontrado 3 alumnos sin DNI, salimos del bucle
    if studentsWithoutDNI == 3:
        break

    # block 0: El usuario ingresa nuevamente la edad y el pais
    age = int(input('Ingresa tu edad: '))
    country = input('Introduzca su pais: ')
    
    # block 1: Mismos controles de elegebilidad de alcohol
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        # Incrementar el contador si el estudiante no puede comprar alcohol
        studentsWithoutDNI += 1 
        print('You can\'t buy alcohol')

# Otro bucle for para iterar sobre 100 estudiantes
studentsWithoutDNI = 0
for student in range(100):

    # Ingrese la edad y el pais de cada estudiante
    age = int(input('Ingresa tu edad: '))
    country = input('Introduzca su pais: ')
    
    # Comprueba si el pais es "USA"
    if country == "USA":
        print('You are not from COL, please come next student')
        continue  # Omite el resto del bucle para esta iteracion y pasa al siguiente estudiante

    # Comprueba si la edad es 15 o menos
    if age <= 15:
        print('You can\'t buy alcohol')
        print('You are still in secondary you cant register to the university')
        continue  # Saltar a la siguiente iteracion si el estudiante esta en secundaria

    # Condicion para asignar un DNI y determinar la elegibilidad universitaria
    hasDegree = False
    if age >= 18 and country == "COL" and hasDegree:
        print("Asigne un DNI")
        print("You can buy alcohol in COL")
        print("You are in the university")
        break  # Romper el ciclo una vez que un estudiante cumple con todos los criterios y se le ha asignado un DNI 


    
    


    
