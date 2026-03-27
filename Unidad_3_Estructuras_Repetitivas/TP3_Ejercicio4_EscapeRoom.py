import random
import string
# Ejercicio N° 4 - Escape Room - La Boveda
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
anti_span = False
cont_span = 0
bloqueado = False

AgenteNombre = input("Ingrese el nombre del agente: \n")
while not AgenteNombre.isalpha():
    print("Error: Nombre invalido")
    AgenteNombre = input("Ingrese el nombre del agente: \n")

while energia > 0 and tiempo >= 0 and cerraduras_abiertas < 3 and not bloqueado:

    print(f"*** Energia: {energia} - Tiempo: {tiempo} - Cerraduras Abiertas: {cerraduras_abiertas}")

    opcionElegida = input("Ingresar una opción:\n1) - Forzar Cerradura.\n2) - Hackear Panel.\n3) - Descansar\n")
    while not opcionElegida.isdigit() or opcionElegida not in ["1", "2", "3"]:
        print("Error: Opción inválida.")
        opcionElegida = input("Ingresar una opción:\n1) - Forzar Cerradura.\n2) - Hackear Panel.\n3) - Descansar\n")
    opcionElegida = int(opcionElegida)

    
    if( opcionElegida == 1):
        energia -= 20
        tiempo -= 2
        anti_span = True
        if(anti_span):
            cont_span += 1
        if energia <= 40:
            print(f"Energia baja: {energia}, Riesgo de alarma")

        if cont_span >=3:
            print("La cerradura se trabó, activaste la alarma")
            alarma = True
            continue

        numeroElegido = input("Ingresar un numero del (1 - 3)\n")
        while not numeroElegido.isdigit() or numeroElegido not in ["1", "2", "3"]:
            print("Error: Opción inválida.")
            numeroElegido = input("Ingresar un numero del (1 - 3)\n")
        numeroElegido = int(numeroElegido)

        if numeroElegido == 3:
            alarma = True
        else:
            print("Cerradura abierta")
            cerraduras_abiertas += 1 

    elif (opcionElegida == 2):
        anti_span = False
        energia -= 10
        tiempo -= 3

        for i in range(4):
            codigo_parcial += random.choice(string.ascii_uppercase)
        print(f"*** codigo_parcial: {codigo_parcial}")

        if(len(codigo_parcial) >= 8):
            print("Cerradura Abierta")
            cerraduras_abiertas +=1
            continue

    elif (opcionElegida == 3):
        anti_span = False
        tiempo -= 1
        if(alarma):
            energia -=10
        else:
            if (energia >= 100):
                continue
            else:
                energia += 15
    if (tiempo <= 3 and alarma == True):
        print("Bloqueado, perdiste!")
        bloqueado == True

    if(anti_span == False):
        cont_span = 0

if(cerraduras_abiertas >= 3 and tiempo > 0):
    print(f"El agente {AgenteNombre}, logro abrir {cerraduras_abiertas} cerraduras")
elif(tiempo == 0 or energia == 0):
    print(f"{AgenteNombre}, perdiste, Game Over")