import csv
import math
var_menu = True

def menu():
    print("1) Filtro palara")
    print("2) Promedio por consola")
    print("3)Cantidad por año")
    print("4)Salir")

def filtrar_archivo(filtro):
    with open('juegos.csv',mode="r",newline='') as archivo:
        data = csv.reader(archivo)
        cadena_guardar =""
        for juego in data:
            if filtro.capitalize() in juego[0]:
                cadena_guardar += juego[0]+ "------>"+juego[-2] +"\n" 
        
        print(cadena_guardar)

        with open("filtro_por_nombre.txt","w") as archivo_a_guardar:
            archivo_a_guardar.write(cadena_guardar)

def promedio_precio_consola(consola):

    with open('juegos.csv',mode="r",newline='') as archivo:
        data = csv.reader(archivo)
        precio_juegos =0.0
        contador=0
        for juego in data:
            if consola.capitalize() in juego[3]:
                precio_juegos += float(juego[2])
                contador +=1

        promedio = precio_juegos/contador
        print(f"EL precio promedio de los juegos de la consola X360 es", promedio.__round__(2))
        
     
    
while var_menu:
    menu()
    opcion = input("Ingrese una opcion")

    if opcion =="4":
        var_menu = False
    elif opcion =="1":
        filtrado = input("Ingrese una palabra clave para filtrar por nombre")
        filtrar_archivo(filtrado)
    elif opcion == "2":
        consola  = input("Ingrese el nombre de una consola para obtener el promedio")
        promedio_precio_consola(consola)
    elif opcion =="3":
        print("tercera")