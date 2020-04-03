import time
import os
try:
    #Opción 1 Añadir provincias y datos
    def Introducir_provincias(lista_provincias):
        provincia=input("Introduzca el nombre de la provincia : ")
        lista_provincias.append(provincia)
        return (lista_provincias)

    def Introducir_casos_confirmados(lista_confirmados):
        caso_confirmado=int(input("Introduzca los casos confirmados : "))
        lista_confirmados.append(caso_confirmado)
        return (lista_confirmados)
    
    def Introducir_casos_nuevos(lista_nuevos):
        caso_nuevo=int(input("Introduzca los casos nuevos : "))
        lista_nuevos.append(caso_nuevo)
        return (lista_nuevos)

    #Listas vacías
    lista_provincias=[]
    lista_confirmados=[]
    lista_nuevos=[]

    #Opción 2 Modificar los datos de una provincia
    def Modificar_casos(lista_provincias,lista_confirmados,lista_nuevos):
        provincia=input("Introduce el nombre de la provincia : ")
        if provincia in lista_provincias: 
            casos_confirmados_Nuevo=int(input("Introduce los cambios a casos confirmados : "))
            casos_nuevos_Nuevo=int(input("Introduce los cambios a casos nuevos : "))
            indice=lista_provincias.index(provincia)
            lista_confirmados[indice]=casos_confirmados_Nuevo
            lista_nuevos[indice]=casos_nuevos_Nuevo
            print("La provincia ",provincia,"tiene ",lista_confirmados[indice]," casos confirmados y hay ",lista_nuevos[indice]," casos nuevos")
        else: 
            print("Esa provincia no se encuentra en la lista")
            input("\nPulse una tecla para continuar ....")
    
    #Opción 3 Imprimir la suma de todo por pantalla
    def Visualizar_todos(lista_confirmados,lista_nuevos):
        print("En Castilla y León el total de casos confirmados es de ",sum(lista_confirmados),"y el total de nuevos casos es de ",sum(lista_nuevos))

        input("\nPulse una tecla para continuar ....")

    #Opción 4 Imprimir todas las provincias por pantalla
    def Visualizar_casos(lista_provincias,lista_confirmados,lista_nuevos):
        n_elementos_lista=len(lista_provincias)
        print("El número de elementos de la lista según la función len es", n_elementos_lista)
        print("LISTADO DE PROVINCIAS CON CASOS CONFIRMADOS Y CASOS NUEVOS DE CORONAVIRUS")
        print("-------------------------------------------------------------------------")
        for indice in range(0,n_elementos_lista):
            print(lista_provincias[indice],"\t",lista_confirmados[indice],"\t",lista_nuevos[indice])
            
        input("\nPulse una tecla para continuar ....")

    while True:
        os.system ("cls")  
        print("Situación epidemiológica del coronavirus (COVID-19) en Castilla y León ")
        print ("Actualización diaria. Datos a ",time.strftime("%d/%m/%y"))
        print("\t1.- Dar de alta  Provincia y datos (confirmados y nuevos)")#añadir provincia y datos
        print("\t2.- Introduce una provincia para modificar sus datos(confirmados y nuevos) " )#modificar datos de una provincia
        print("\t3.- Numero Total de casos Confirmados y Nuevos en la Comunidad ")#listar todo de una comunidad
        print("\t4.- Listado de la situacion  general por provincias(confirmados y nuevos)")#listar todos
        print("\t5.- Salir")
        print("")
        opcion=int(input("Introduce la opcion que deseas :"))
        if opcion==1:
            lista_provincias=Introducir_provincias(lista_provincias)
            lista_confirmados=Introducir_casos_confirmados(lista_confirmados)    
            lista_nuevos=Introducir_casos_nuevos(lista_nuevos)      
        elif opcion==2:
            Modificar_casos(lista_provincias,lista_confirmados,lista_nuevos)
        elif opcion==3:
            Visualizar_todos(lista_confirmados,lista_nuevos)
        elif opcion==4:
            Visualizar_casos(lista_provincias,lista_confirmados,lista_nuevos)
        else:
            break

except ValueError:
    print("No pude convertir el dato a un entero.")
except Exception as e: # OJO SIEMPRE LA ULTIMA
    print("Ha ocurrido un error no previsto del tipo ", type(e).__name__ )
