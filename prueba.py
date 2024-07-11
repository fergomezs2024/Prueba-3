import csv
var_menu = True

def menu():
    print("1) Filtro palara")
    print("2) Promedio por consola")
    print("3)Cantidad por año")
    print("4)Salir")

def filtrar_archivo():
    with open('juegos.csv',mode="r",newline='') as archivo:
        data = csv.reader(archivo)
        print(data)
    
while var_menu:
    menu()
    opcion = input("Ingrese una opcion")

    if opcion =="4":
        var_menu = False
    elif opcion =="1":
        filtrado = input("Ingrese una palabra clave para filtrar por nombre")
        filtrar_archivo()
    elif opcion == "2":
        consola  = input("Ingrese el nombre de una consola para obtener el promedio")
    elif opcion =="3":
        print("tercera")