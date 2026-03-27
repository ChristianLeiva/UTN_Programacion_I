# # Actividad N° 1:
# edad = int(input("Ingrese su edad: "))
# respuesta = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
# print(respuesta)
# # ----------------------------

# # Actividad N° 2:
# nota = float(input("Ingrese la nota del estudiante (0-10): "))
# respuesta = "Aprobado" if nota >= 6 else "Reprobado"
# print(respuesta)
# # ----------------------------

# # Actividad N° 3: Números pares
# numero = int(input("Ingrese un número entero: "))
# respuesta = "El número es par" if numero % 2 == 0 else "El número es impar"
# print(respuesta)
# # ----------------------------

# # Actividad N° 4: Edad
# edad = int(input("Ingrese su edad: "))
# if edad < 12:
#     print("Niño")
# elif edad >= 12 and edad < 18:
#     print("Adolescente")
# elif edad >= 18 and edad < 30:
#     print("Adulto/a joven")
# elif edad >= 30:
#     print("Adulto/a")
# # ----------------------------

# # Actividad N° 5: Constraseña correcta
# password = input("Ingrese la contraseña debe tener entre 8 y 14 caracteres:\n")
# if len(password) >= 8 and len(password) <= 14:
#     print("Ha ingresado una Contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# # ----------------------------

# # Actividad N° 6: Consumo de energía
# consumo = float(input("Ingrese el consumo de energía en kWh: "))
# if consumo < 150:
#     print("Consumo bajo")
# elif consumo >= 150 and consumo < 300:
#     print("Consumo medio")
# elif consumo >= 300 and consumo < 500:
#     print("Consumo alto")
# elif consumo >= 500:
#     print("Considere medidas de ahorro energético")
# # ----------------------------

# # Actividad N° 7: vocal
# frase = input("Ingrese una palabra: ").lower()
# ultima_letra = frase[-1]
# # if ultima_letra == 'a' or ultima_letra == 'e' or ultima_letra == 'i' or ultima_letra == 'o' or ultima_letra == 'u':
# if ultima_letra in ['a', 'e', 'i', 'o', 'u']:
#     print(frase + "!")
# else:
#     print(frase)
# # ----------------------------

# # Actividad N° 8: Opcion Nombre
# nombre = input("Ingrese su nombre: ").lower()
# opcion = int(input("Ingrese una opcion:\n1 - Nombre en Mayuscula\n2 - Nombre en Minuscula\n3 - Nombre en Capitalize\n"))
# if opcion == 1:
#     print(nombre.upper())
# elif opcion == 2:
#     print(nombre.lower())
# elif opcion == 3:
#     print(nombre.capitalize())
# else:
#     print("Opción no válida")
# # ----------------------------

# # Actividad N° 9: Magnitud de un terremoto
# magnitud = int(input("Ingrese la magnitud del terremoto: "))
# if magnitud < 3:
#     print('"Muy leve" (Imperceptible)')
# elif magnitud >= 3 and magnitud < 4:
#     print('"Leve" (Ligeramente perceptible)')
# elif magnitud >= 4 and magnitud < 5:
#     print('"Moderado" (Sentido por personas, pero generalmente no causa daños')
# elif magnitud >= 5 and magnitud < 6:
#     print('"Fuerte" (puede causar daños en estructuras débiles)')
# elif magnitud >= 6 and magnitud < 7:
#     print('"Muy Fuerte" (puede causar daños significativos)')
# elif magnitud >= 7:
#     print('"Extremo" (puede causar graves daños a gran escala)')
# # ----------------------------

# # Actividad N° 10: Estacion del año
# emisferio = input("Ingrese su hemisferio (N/S): ").lower()
# mes = int(input("Ingrese el número del mes (1-12): "))
# dia = int(input("Ingrese el día del mes (1-31): "))

# if emisferio == 'n':
#     if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia < 20)):
#         print("Es invierno")
#     elif (mes == 3 and dia >= 20) or (mes <= 6 and (mes != 6 or dia < 21)):
#         print("Es primavera")
#     elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 9 or dia < 22)):
#         print("Es verano")
#     elif (mes == 9 and dia >= 22) or (mes <= 12 and (mes != 12 or dia < 21)):
#         print("Es otoño")
# elif emisferio == 's':
#     if (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 9 or dia < 22)):
#         print("Es invierno")
#     elif (mes == 9 and dia >= 22) or (mes <= 12 and (mes != 12 or dia < 21)):
#         print("Es primavera")
#     elif (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia < 20)):
#         print("Es verano")
#     elif (mes == 3 and dia >= 20) or (mes <= 6 and (mes != 6 or dia < 21)):
#         print("Es otoño")
# else:
#     print("Hemisferio no válido")
# # ----------------------------