PrecioAsiento_normal= 78900
PrecioAsiento_vip=240000
informacion_clientes=[[]
]
lista_asientoOcupados=[]
matriz_asientos=[
    [" ",1," ",2," ",3," "," ",4," ",5," ",6," "      ,],
    [" ",7," ",8," ",9," "," ",10," ",11," ",12," ",   ],
    [" ",13," ",14," ",15," "," ",16," ",17," ",18," ",],
    [" ",19," ",20," ",21," "," ",22," ",23," ",24," ",],
    [" ",25," ",26," ",27," "," ",28," ",29," ",30," ",],
    ["____________________","","______________________"],
    [" ",31," ",32," ",33," "," ",34," ",35," ",36," ",],
    [" ",37," ",38," ",39," "," ",40," ",41," ",42," ",],
    ]
#----------------------------------------------------------------------------------------------
def ver_asientos():
    for elementos in matriz_asientos :
        print(elementos)



#-------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------ - 
def comprar_Asiento():
    Nombre_Pasajero=input("Ingrese su Nombre : ")
    Rut_Pasajero=input("Ingrese su Rut : ")
    while True:
        Telefono_Pasajero=input("Ingrese Numero de Telefono : ")
        if Telefono_Pasajero.startswith("9")and len(Telefono_Pasajero)  :
            print("Numero Ingresado correctamente")
            break
        else:
            print("El numero ingresado es incorrecto,le falta agregar el 9 ")
    
    Banco_Pasajero=input("Ingrese Banco : ")
    if Banco_Pasajero == "bancoDUOC".lower() : 
            print("Usted tiene un 15% de descuento")
            descuento = 0.15 
    else:
            print("No posee ningun descuento")
            descuento= 0
    print("Asientos ocupados:", lista_asientoOcupados) 
    Numero_asiento=int(input("Ingrese un asiento disponible: "))
    if Numero_asiento in lista_asientoOcupados:
        print("Asiento NO disponible")
    else:
        lista_asientoOcupados.append(Numero_asiento)
        print("Asiento  Disponible")
    pasajero=([Nombre_Pasajero,Rut_Pasajero,Telefono_Pasajero,Numero_asiento])
    informacion_clientes.append(pasajero)  
    if Numero_asiento >= 31 and Numero_asiento < 43 :
        preciototal = PrecioAsiento_vip*(1-descuento) #100-15
        print("Asiento VIP con un precio de $",preciototal)  
    else:
            preciototal=PrecioAsiento_normal*(1-descuento)
            print("Asiento Normal con un precio de $",preciototal)
 #----------------------------------------------------------------------------------------         

def modificar_datos():
    Rut_pasajero=input("Ingrese rut : ")
    Numero_asiento=int(input("Ingrese el numero del asiento"))
    for columna in informacion_clientes:
        if columna[1] == Rut_pasajero: 
             print("Datos a Modificar")          
    while True:
        Nombre_pasajero=input("Ingrese su nombre: ")
        Telefono_Pasajero=int(input("Ingrese numero telefono: "))
        if Telefono_Pasajero.startswith("9") and len(Telefono_Pasajero):
            print("Telefono agregado con exito")
            columna[0]= Nombre_pasajero
            columna[2]=Telefono_Pasajero
            break
        else:
             print("El numero debe empezar con 9 y tener 9 digitos")    
        pasajero=([Nombre_pasajero,Rut_pasajero,Telefono_Pasajero,Numero_asiento])
        informacion_clientes.append(pasajero)
         

#----------------------------------------------------------------------------------------
def anular_viaje():
     Numero_asiento=int(input("Ingrese numero de asiento: "))
     if Numero_asiento in informacion_clientes :
        informacion_clientes.remove(Numero_asiento)
        print("Informacion eliminada")
        for pasajero in informacion_clientes:
            if pasajero[3]== Numero_asiento :
                informacion_clientes.remove(pasajero)
                print("Informacion eliminada")
                
while True :

    print("     Menu        ")
    print("*****************")
    print("1. Ver Asientos Disponibles")
    print("2. Comprar Asiento")
    print("3. Anular Vuelo")
    print("4. Modificar Datos de Pasajeros")
    print("5. Salir")
    opcion=int(input("Ingrese una Opcion del 1 al 5 : "))
    if opcion == 1 :
         print(" Visualizacion de Asientos Disponibles")
         ver_asientos()
         
    elif opcion == 2 :
        print("Compra de Asientos")
        comprar_Asiento()
        
    elif opcion == 3 :
        print("Anular Vuelo")
        anular_viaje()
    elif opcion == 4 :
        print("Modificar Datos de Pasajeros")
        modificar_datos()
    elif opcion == 5 :
        print("Saliendo.....")
        break
    
print(informacion_clientes)
    
        