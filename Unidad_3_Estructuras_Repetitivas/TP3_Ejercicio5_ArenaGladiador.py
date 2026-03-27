import random
# Ejercicio N° 5 - Escape Room - La Arena - Gladiador
vidaGladiador=100
vidaEnemigo=100  
pocionesVida=3  
dañoBase=15  
dañoBaseEnemigo=12  
turnoGladiador =True

print("*** Bienvenido a la arena ***")
gladiador = input("Ingrese el nombre del gladiador:\n")
while (not gladiador.isalpha()):
    print("Error: Nombre invalido")
    gladiador = input("Ingrese el nombre del gladiador:\n")

print("*** Inicio de la batalla ***")
while vidaGladiador > 0 and vidaEnemigo > 0:
    print(f"{gladiador} (HP: {vidaGladiador}) vs Enemigo (HP: {vidaEnemigo}) | Pociones: {pocionesVida}")
    
    if(turnoGladiador):
        opcionElegida = input("Ingresar una opción:\n1) - Ataque Pesado.\n2) - Rafaga Veloz.\n3) - Curar\n")
        while not opcionElegida.isdigit() or opcionElegida not in ["1", "2", "3"]:
            print("Error: Opción inválida.")
            opcionElegida = input("Ingresar una opción:\n1) - Ataque Pesado.\n2) - Rafaga Veloz.\n3) - Curar\n")
        opcionElegida = int(opcionElegida)

        if(opcionElegida == 1):
            if vidaEnemigo <= 20:
                print("Golpe Crítico")
                daño = dañoBase * 1.5
            else:
                daño = dañoBase
            print(f"Atacaste al enemigo por {daño} puntos de daño")
            vidaEnemigo -= daño
        if(opcionElegida == 2):
            for i in range(3):
                daño = random.randint(1, 5)
                print(f"Atacaste al enemigo por {daño} puntos de daño")
                vidaEnemigo -= daño
        if(opcionElegida == 3):
            if(pocionesVida > 0):
                vidaGladiador += 30
                pocionesVida -= 1
            else:
                print("No quedan posiones!")
                continue
        
        turnoGladiador = False
    else:
        print(f"¡El enemigo te atacó por {dañoBaseEnemigo} puntos de daño!")
        vidaGladiador -= dañoBaseEnemigo
        turnoGladiador = True

if(vidaGladiador > 0):
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
else:
    print(f"DERROTA. {gladiador} ha caído en combate.")



