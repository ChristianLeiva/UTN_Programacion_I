# Ejercicio N° 2 - Acceso al Campus y Menú seguro
# 1. Definir credenciales fijas en el código:
#   - usuario correcto: "alumno"
#   - clave correcta: "python123"
# 2. Permitir máximo 3 intentos para ingresar usuario y clave.
# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#   - 1. Ver estado de inscripción (mostrar “Inscripto”)
#   - 2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
#   - 3. Mostrar mensaje motivacional (1 frase)
#   - 4. Salir
# 5. Validación del menú:
#   - Debe ser número (.isdigit())
#   - Debe estar entre 1 y 4
#   - Cambio de clave
#   - La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, rechazar.

alumno = {
"usuario": "alumno",
"password": "python123",
"nombre" : "Pepe"
}
cont = 0

print("*** Bienvenido al Campus ***")

for i in range(3):
    usuario = input(f"Intento {i+1}/3: Ingrese su usuario: ")
    password = input(f"Intento {i+1}/3:Ingresar el password: ")
    if(usuario == alumno["usuario"] and password == alumno["password"]):
        print("*** Acceso Concedido ***")
        opcionElegida = 0 
        while opcionElegida != "4":
            opcionElegida = input("Ingrese una opción:\n1)-Estado de la inscripción. \n2)-Cambio de clave. \n3)-Frase motivacional. \n4)-Salir.\n")
            while (not opcionElegida.isdigit() or opcionElegida not in ["1", "2", "3", "4"]):
                print("Error: ingrese un número valido")
                opcionElegida = input("Ingrese una opción:\n1)-Estado de la inscripción. \n2)-Cambio de clave. \n3)-Frase motivacional. \n4)-Salir.\n")
            if(int(opcionElegida) == 1):
                print(f"*** El alumno {alumno['nombre']} está inscripto ***")
            elif(int(opcionElegida) == 2):
                print("*** Cambio de clave ***")
                claveNueva = input("Ingrese la clave nueva. Minimo 6 caracteres. ***")
                while len(claveNueva) < 6:
                    print("Error: La clave debe tener minimo 6 caracteres.")
                    claveNueva = input("Ingrese la clave nueva. Minimo 6 caracteres. ***")
                
                confirmarClave = input("Confirmar clave nueva. ***")
                if(claveNueva != confirmarClave): 
                    print("*** Error: las claves no coinciden. ***")
                else:
                    alumno["password"] = claveNueva
                    print(alumno)
                    print("*** La clave se cambio con exito. ***")
            elif(int(opcionElegida) == 3):
                print("*** Frase motivacional. ***\n 'Programar no se trata de lo que sabes, sino de lo que puedes resolver'")
        break
    else:
        print("Error: Credenciales invalidas")
        cont += 1
        
if (cont == 3):
    print("Error: Maximo de intentos permitidos, usuario bloqueado")