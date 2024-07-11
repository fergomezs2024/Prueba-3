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

        if len(cadena_guardar) != 0:
            with open("filtro_por_nombre.txt","w") as archivo_a_guardar:
                archivo_a_guardar.write(cadena_guardar)
            return True
        else:
            
            return False

def promedio_precio_consola(consola):

    with open('juegos.csv',mode="r",newline='') as archivo:
        data = csv.reader(archivo)
        precio_juegos =0.0
        contador=0
        for juego in data:
            if consola.capitalize() in juego[3]:
                precio_juegos += float(juego[2])
                contador +=1
        if contador !=0:
            promedio = precio_juegos/contador
            print(f"EL precio promedio de los juegos de la consola X360 es", promedio.__round__(2))
            return True
        else:
            return False

def filtrar_juegos_por_anio(anios):
    with open('juegos.csv',mode="r",newline='') as archivo:
        data = csv.reader(archivo)
        contadorpsps=0
        contadorx360=0
        contadorDs=0
        contadorps3=0
        contadorWii=0
        cadena_a_guardar =""
        consolas = []
        for juego in data:
            if anios == juego[-1]:
                consolas.append(juego[-2])
                len(juego[-2])

 
        for conso in consolas:
            if conso == "Sony PSP":
                contadorpsps+=1
            if conso =='X360':
                contadorx360+=1
            if conso == 'Nintendo DS':
                contadorDs+=1
            if conso =='PlayStation 3':
                contadorps3+=1
            if conso =='Nintendo Wii':
                contadorWii+=1
            
        if contadorDs >0 :
            cadena_a_guardar += (f"La consola  nintendo ds tuvo {contadorDs} juegos\n")
        if contadorpsps >0:
            cadena_a_guardar += (f"La consola  psp tuvo {contadorpsps} juegos \n")
        if contadorx360 >0:
            cadena_a_guardar += (f"La consola  xbox360 tuvo {contadorx360} juegos \n")
        if contadorps3 >0:
            cadena_a_guardar += (f"La consola  playstation 3 tuvo {contadorps3} juegos \n")
        if contadorWii >0:
            cadena_a_guardar += (f"La consola  nintendo wii tuvo {contadorWii} juegos \n")

        with open(f"juegos_{anios}","w") as arch:
            arch.write(cadena_a_guardar)
        
     
    
while var_menu:
    menu()
    opcion = input("Ingrese una opcion")

    if opcion =="4":
        var_menu = False
    elif opcion =="1":
        filtrado = input("Ingrese una palabra clave para filtrar por nombre")
        try:
            res = filtrar_archivo(filtrado)
            if res :
                print("Archivo creado exitosamente!!")
            else:
                print("No se han encontrado juegos con ese nombre: ")

        except:
            print("No se ha logrado crear el archivo")

    elif opcion == "2":
        consola  = input("Ingrese el nombre de una consola para obtener el promedio: ")
        res = promedio_precio_consola(consola)

        if res:
            print("wiii")
        else:
            print("boo")

    elif opcion =="3":
        anio = input("Ingrese año para buscar juegos: ")
        res = filtrar_juegos_por_anio(anio)