# Ejercicio N° 3 - Agenda de turnos con nombres

lunes = ["vacio", "vacio", "vacio", "vacio"]
martes = ["vacio", "vacio", "vacio"]
paciente = ""
contL = 0 
contM= 0

operador = input("Nombre del operador:\n")
while (not operador.isalpha()):
    print("Error: Nombre invalido")
    operador = input("Nombre del operador:\n")
opcionMenu = ""
while opcionMenu != "5":

    opcionMenu = input("\nIngrese una opción:\n1)-Reservar turno.\n2)-Cancelar turno.\n3)-Ver agenda del día.\n4)-Ver resumen general.\n5)-Cerrar sistema.\n- ")
    while not opcionMenu.isdigit() or opcionMenu not in ["1", "2", "3", "4", "5"]:
        print("Error: Opción Inválida.")
        opcionMenu = input("\nIngrese una opción:\n1)-Reservar turno.\n2)-Cancelar turno.\n3)-Ver agenda del día.\n4)-Ver resumen general.\n5)-Cerrar sistema.\n- ")

    if opcionMenu == "1":
        print("*** Reservar turno ***")
        diaTurno = int(input("Elija:\n1)-Lunes\n2)-Martes:\n"))
        while diaTurno not in [1, 2]:
            print("Error: Opción Invalida")
            diaTurno = int(input("Elija:\n1)-Lunes\n2)-Martes:\n"))

        paciente = input("Nombre del paciente:\n")
        while (not paciente.isalpha()):
            print("Error: Nombre invalido")
            paciente = input("Nombre del paciente:\n")

        if (diaTurno == 1):
            sinturno = False
            for turno in range(len(lunes)):
                if(paciente.lower() in lunes[turno].lower()):
                    print(f"Error: El paciente: {paciente} ya tiene un turno cargado")
                if(lunes[turno] == "vacio"):
                    lunes[turno] =f"Lunes {turno+1} - {paciente}"
                    sinturno = True
                    break
            if not sinturno:
                print("Error: No hay turnos disponibles el dia Lunes")
        elif (diaTurno == 2):
            sinturno = False
            for turno in range(len(martes)):
                if(paciente.lower() in martes[turno].lower()):
                    print(f"Error: El paciente: {paciente} ya tiene un turno cargado")
                if(martes[turno] == "vacio"):
                    martes[turno] =f"Martes {turno+1} - {paciente}"
                    sinturno = True
                    break
            if not sinturno:
                print("Error: No hay turnos disponibles el dia Martes")
    # *******************************************************************
    elif opcionMenu == "2":
        print("*** Cancelar turno ***")
        paciente = input("Nombre del paciente:\n")
        while (not paciente.isalpha()):
            print("Error: Nombre invalido")
            paciente = input("Nombre del paciente:\n")
        for l in range(len(lunes)):
            sinturno = True
            if(paciente.lower() in lunes[l].lower()):
                lunes[l] = "vacio"
                print(f"Turno del paciente: {paciente} cancelado.")
                sinturno = False
                break
        for m in range(len(martes)):
            sinturno = True
            if(paciente.lower() in martes[m].lower()):
                martes[m] = "vacio"
                print(f"Turno del paciente: {paciente} cancelado.")
                sinturno = False
                break
        if(sinturno):
            print(f"No se encontraron turnos al nombre de: {paciente}")
    # *******************************************************************   
    elif opcionMenu == "3":
        print("*** Ver agenda del día ***")
        diaTurno = int(input("Elija:\n1)-Lunes\n2)-Martes:\n"))
        while diaTurno not in [1, 2]:
            print("Error: Opción Invalida")
            diaTurno = int(input("Elija:\n1)-Lunes\n2)-Martes:\n"))
        if(diaTurno == 1):
            for l in range(len(lunes)):
                print(lunes[l])
        elif(diaTurno == 2):
            for m in range(len(martes)):
                print(martes[m])
    # ******************************************************************* 
    elif opcionMenu == "4":        
        print("Turnos del día Lunes:\n")
        for l in range(len(lunes)):
            print(lunes[l])
            if(lunes[l] != "vacio"):
                contL += 1
        print("\nTurnos del día Martes:\n")
        for m in range(len(martes)):
            print(martes[m])
            if(martes[m] != "vacio"):
                contM += 1

        if(contL > contM):
            print(f"El dia Lunes tiene más días con turnos reservados: {contL}")
        elif(contM > contL):
            print(f"El dia Martes tiene más días con turnos reservados: {contM}")
        elif(contL == contL):
            print(f"Ambos días tienen la misma cantidad de turnos reservados: {contM}")

    elif opcionMenu == "5":
        print(f"*** Cerrando sistema. Hasta luego {operador}! ***")
