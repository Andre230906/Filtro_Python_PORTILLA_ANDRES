import json
import os

def limpiar_terminal():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def add_CLIENTEs():
    limpiar_terminal()
    print("""
            **********************
            *                    *
            * MOVISTAR CLIENTES  *
            *                    *
            **********************
            """)
    
    
    ******

    
    with open("file.json", "r") as outfile:
        Data = json.load(outfile)

    newc = {}
    newc["ID"] = int(input("*Ingrese el ID del cliente "))
    newc["nombres"] = input("*Ingrese los nombres del cliente                                    : ")
    newc["apellido"] = input("*Ingresa los apellidos del cliente                                 : ")
    newc["ciudad"] = input("*Ingrese la ciudad del cliente                                       : ")
    newc["fecha"] = input("*Ingrese la fecha de inicio del cliente                               : ")
    newc["N_celular"] = input("*Ingrese la fecha de inicio del cliente                           : ")


    Data["file.json"].append(newc)

    with open("file.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)
      
def actualizar_datos_CLIENTE():
    limpiar_terminal()
    print("""
            **********************
            *                    *
            *ACTUALIZAR PACIENTE *
            *                    *
            **********************
            """)
    edit = open("filejson")
    Data = json.load(edit)
    CLIENTES = Data["CLIENTE"]
    IDi_CLIENTE = int(input("Ingresa el id del paciente a actualizar: "))
    for CLIENTE in CLIENTES:
        if CLIENTE["ID"] == IDi_CLIENTE:
            
            nombres = input("Ingresa los nuevos nombres: ") 
            apellidos = input("Ingresa los nuevos apellidos: ")
            ciudad = input("Ingresa la ciudad a cambiar: ")
            Direccion = input("Ingrese la direccion a cambiar: ")
            Acudiente = input("Ingresa el acudiente a cambiar : ")
            N_celular = input("Ingresa el nuevo numero de celular: ")
            N_fijo = input("Ingresa el nuevo numero de teléfono fijo: ")
            
            CLIENTE["nombres"] = nombres
            CLIENTE["apellido"] = apellidos
            CLIENTE["ciudad"] = ciudad
            CLIENTE["Direccion"] = Direccion
            CLIENTE["Acudiente"] = Acudiente
            CLIENTE["Fecha"] = N_celular
            CLIENTE["N_celular"] = N_celular


    
    with open("JSON/CLIENTEs.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)
        
def imprimir_todos_los_CLIENTEs():
    limpiar_terminal()
    print("""
            **********************
            *                    *
            *  IMPRIMIR CLIENTES  *
            *                    *
            **********************
            """)
    try:
        with open('file.json', 'r') as archivo:
            datos = json.load(archivo)
            a = int(input("Ingresa (1) para continuar: "))
            if a == 1:
                for CLIENTE in datos['CLIENTE']:
                    print("ID: ", CLIENTE['ID']) # Agrega una línea en blanco entre cada CLIENTE
                    print("Nombres: ", CLIENTE['nombres'])
                    print("Apellido:", CLIENTE['apellido'])
                    print("Ciudad:", CLIENTE['ciudad'])
                    print("N_celular:", CLIENTE['N_celular'])
                    print("N_fijo:", CLIENTE['N_fijo'])
                    print("")

                  # print(f"ID: {CLIENTE['ID']}, nombres: {CLIENTE['nombres']}, Apellido: {CLIENTE['apellido']}, ciudad: {CLIENTE['ciudad']}, direccion: {CLIENTE['Direccion']}, Acudiente: {CLIENTE['Acudiente']}, Ncelular: {CLIENTE['N_celular']}, Nfijo: {CLIENTE['N_fijo']}, Estado: {CLIENTE['Estado']}")
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        
def listar_CLIENTEs_por_estado(estado):
    limpiar_terminal()
    print("""
            **********************
            *                    *
            * LISTAR POR CLIENTE *
            *                    *
            **********************
            """)
    with open('file.json') as f:
        data = json.load(f)
        CLIENTEs = data['CLIENTE']

    CLIENTEs_segun_estado = [CLIENTE for CLIENTE in CLIENTEs if CLIENTE['Estado'] == estado]

    if CLIENTEs_segun_estado:
        print(f"CLIENTEs con estado '{estado}':")
        for CLIENTE in CLIENTEs_segun_estado:
            print("")
            print("ID:", CLIENTE['ID'])
            print("Nombre:", CLIENTE['nombres'])
            print("Apellido:", CLIENTE['apellido'])
            print("Ciudad:", CLIENTE['ciudad'])
            print("Dirección:", CLIENTE['Direccion'])
            print("Acudiente:", CLIENTE['Acudiente'])
            print("Número celular:", CLIENTE['N_celular'])
            print("Número fijo:", CLIENTE['N_fijo'])
            print("Estado:", CLIENTE['Estado'])
            print()  # Imprimir una línea en blanco entre cada CLIENTE
    else:
        print(f"No hay CLIENTEs con estado '{estado}'.")
        
def ev_CLIENTE():
    limpiar_terminal()
    print("""
            **********************
            *                    *
            *  NOTAS    CLIENTES  *
            *                    *
            **********************
            """)
    edit = open("JSON/CLIENTEs.json")
    Dat = json.load(edit)
    camp = Dat["CLIENTEs"]
    ID_CLIENTE = int(input("Ingrese el número de identificación del CLIENTE que desea hallar su calificacion final:"))
    for camp in camp:
        if camp["ID"] == ID_CLIENTE:  
            teo = float(input("Ingrese promedio de notas de la teorica: "))
            pra = float(input("Ingrese promedio de notas de la practica: "))
            pro = float(input("Ingrese promedio da la procedimental: "))
            final = (teo *  0.3) + (pra *  0.6) + (pro *  0.1)
            if final >=  65:
                    camp['Estado'] = "Aprobado"  
                    camp["nota"] = ("",final) 
                    print("¡Este CLIENTE ha aprobado el filtro mensual con una nota final de", final)
            elif final >59 & final < 65:
                    camp['Estado'] = "Bajo rendimiento"   
                    camp["nota"] = "la nota es",final
                    print("El CLIENTE esta en riego, Su nota final es", final)
            else:
                    camp['Estado'] = "Reprobado"   
                    camp["nota"] = "la nota es",final
                    print("El CLIENTE no ha aprobado, Su nota final es", final)                    
        else:
           print("CLIENTE no encontrado.")  
           break   
                         
                    
                      
    with open("JSON/CLIENTEs.json", "w") as outfile:
        json.dump(Dat, outfile, indent=4)
        
def admin_menu():
    file_path = 'JSON/CLIENTEs.json'

    print("""
            *********************
            *                   *
            *MENU ADMINISTRACION*
            *                   *
            *********************
            """)
    print("*Agregar CLIENTE       (1)")
    print("*Notas CLIENTE         (2)")
    print("*Actualizar CLIENTE    (3)")
    print("*Listar CLIENTEs       (4)")
    print("*Menu principal        (10)")

    b = int(input("Ingrese la opción deseada: "))
    if b==1:
        add_CLIENTEs()
    elif b==2:
        actualizar_datos_CLIENTE()
    


admin_menu()
