import json
import os

def limpiar_terminal():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")


def menu_principal():
        
    print("""
          ********************************
          *BIENVENIDO AL MENU DE MOVISTAR*
          ********************************
          
        
          """)
    print("     1.modulo de reportes")
    print("     2.modulo de gestion de servicio")
    print("     3.modulo de bonificacion para clientes leales")
    print("     4.cliente")
    print("     4.volver ")
    print("")
    while True:
        try:

            a=int(input("seleccione una opcion del 1-4  "))
            if a==1:
                modulo_reportes()
            elif a==2:
                modulo_gestion()
            elif a==3:
                modulo_bonificacion()
            elif a==4:
                break 
            else:
                menu_principal() 
        except: ValueError         


def modulo_reportes():
    print("""
          ***********************************
          *BIENVENIDO AL MODULO DE REPORTES *
          ***********************************
          """)
    print("     1.Informes de productos")
    print("     2.Analisis de datos ")
    print("     3.informe de usuarios por servicio")
    print("     4.Volver ")
    print("")
    while True:
        try:
            a=int(input("seleccione una opcion del 1-4  "))
            if a==1:
                informe_productos()
            elif a==2:
                Analisis()
            elif a==3:
                informe_servicio()
            elif a==4:
                menu_principal()
            else:
                modulo_reportes()  
        except:ValueError

def modulo_gestion():
    print("""
          ***********************************
          *BIENVENIDO AL MODULO DE GESTION  *
          ***********************************
          """)
    print("     1.Crear servicio    ")
    print("     2.Actualizar servicio ")
    print("     3.Eliminar servicio  ")
    print("     4.Informacion de servicio ")
    print("     5.Volver")
    print("")
    while True:
        try:        
            a=int(input("seleccione una opcion del 1-5  "))
            if a==1:
                Crearservicio()
            elif a==2:
                Actualizarservicio()
            elif a==3:
                Eliminarservicio()
            elif a==4:
                Informacionservicio()  
            elif a==5:
                menu_principal()
            else:
                modulo_gestion()
        except: ValueError
 
def modulo_bonificacion():
    print("""
          ****************************************
          * BIENVENIDO AL MODULO DE BONIFICACION *
          ****************************************
          """)
    while True:
        try:
            print("     1.Identicacion de clientes leales   ")
            print("     2.Bonificacion ")
            print("     3.Asesor de ventas  ")
            print("     4.volver ")
            print("")
            a=int(input("seleccione una opcion del 1-4  "))
            if a==1:
                Identicacionclientes()
            elif a==2:
                Bonificacion()
            elif a==3:
                asesorventas()
            elif a==4:
                menu_principal()  
            else:
                modulo_gestion()
        except: ValueError

#modulo de reportes


def informe_productos():
    print("x")

def Analisis():
    print("x")

def informe_servicio():
    print("x")
#modulo gestion
def Crearservicio():
    print("x")
def Actualizarservicio():
    print("x")
def Eliminarservicio():
    print("x")
def Informacionservicio():
    print("x")
#modulo de bonificacion
def Identicacionclientes():
    print("x")
def Bonificacion():
    print("x")
def asesorventas():
    print("En un momento el asesor se comunicara contigo")

    
menu_principal() 

