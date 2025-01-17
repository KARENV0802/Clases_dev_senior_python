from datetime import datetime
import statistics

from sqlalchemy import true

class Tarea:

    #Funcion de inicializacion = metodo constructor
    def __init__(self, nombre, fecha_limite, categorias, horas_Dedicadas):
        self.nombre = nombre
        self.fecha_limite = fecha_limite
        self.categorias = categorias
        self.horas_Dedicadas = horas_Dedicadas



#Funcion para agregar una tarea
def agregar_tarea(lista_tareas):
    nombre = input("Ingrese el nombre de la tarea: ")
    fecha_limite_str = input("Ingrese la fecha limite de la tarea (DD/MM/YYYY): ")
    try:
        fecha_limite = datetime.strptime(fecha_limite_str, "%d/%m/%Y")
    except ValueError:
        print("Formato de fecha incorrecto")
        return
    
    categorias = input("Ingrese la categoria de la tarea (estudio, personal, trabajo, otras): ")
    horas_Dedicadas_str = input("ingrese las horas dedicadas, separadas en comas: ")
    try:
        horas_Dedicadas = list(map(float, horas_Dedicadas_str.split(',')))
    except ValueError:
        print("Formato de horas dedicadas incorrecto")
        return
    
    #Crear un objeto y lo agrega a la lista de tareas
    tarea = Tarea(nombre, fecha_limite, categorias, horas_Dedicadas)
    lista_tareas.append(tarea)
    print("Tarea agregada exitosamente")

#Funcion para mostrar las tareas
def visualizar_Tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas para mostrar")
        return

    for i, tarea in enumerate(lista_tareas, start=1):
        print(f"\n Tarea {i}")
        print(f"Nombre: {tarea.nombre}")
        print(f"Fecha limite: {tarea.fecha_limite.strftime('%d/%m/%Y')}")
        print(f"Categorias: {tarea.categorias}")
        print(f"Horas dedicadas: {tarea.horas_Dedicadas}")

def analizar_Horas (lista_tareas):
    if not lista_tareas:
        print("No hay tareas para analizar")
        return
    
    for tarea in lista_tareas:
        promedio = statistics.mean (tarea.horas_Dedicadas)
        maximo = max (tarea.horas_Dedicadas)
        minimo = min (tarea.horas_Dedicadas)
        print(f"\n Analisis de {tarea.nombre}")
        print(f"Promedio de horas dedicadas: {promedio}")
        print(f"Maximo de horas dedicadas: {maximo}")
        print(f"Minimo de horas dedicadas: {minimo}")

#Generar informe de tareas
def generar_informe(lista_tareas):
    if not lista_tareas:
        print("No hay tareas para generar informe")
        return

    #abrir un archivo txt para escribir un informe
    with open("informe_tareas.txt", "w") as archivo:
        for tarea in lista_tareas:
            archivo.write(f"\n Nombre: {tarea.nombre}")
            archivo.write(f"\n Fecha limite: {tarea.fecha_limite.strftime('%d/%m/%Y')}")
            archivo.write(f"\n Categorias: {tarea.categorias}")
            archivo.write(f"\n Horas dedicadas: {tarea.horas_Dedicadas}")
            archivo.write("\n")
    print("Informe generado exitosamente")

def menu():
    lista_tareas = []
    while true: 
        print("\nMenu de opciones")
        print("1. Agregar tarea")
        print("2. Visualizar tareas")
        print("3. Analizar horas")
        print("4. Generar informe")
        print("5. Salir")

        opcion = input("Seleccion una opcion: ")

        if opcion == "1":
            agregar_tarea(lista_tareas)
        elif opcion == "2":
            visualizar_Tareas(lista_tareas)
        elif opcion == "3":
            analizar_Horas(lista_tareas)
        elif opcion == "4":
            generar_informe(lista_tareas)
        elif opcion == "5":
            print ("Saliendo del programa")
            break
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    menu()
