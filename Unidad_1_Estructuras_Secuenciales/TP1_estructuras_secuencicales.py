# import math
# # Actividad N° 1

# print("Hola Mundo!")
# # ----------------------------

# # Actividad N° 2

# name = input("Ingresa tu nombre\n")
# print(f"Hola {name}!")
# # ----------------------------

# # Actividad N° 3

# name = input("Ingresa tu nombre\n")
# lastname = input("Ingresa tu apellido\n")
# age = int(input("Ingresa tu edad\n"))
# country = input("Ingresa tu país\n")
# print(f"Soy {name} {lastname}, tengo {age} años y vivo en {country}.")
# # ----------------------------

# # Actividad N° 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
# # Area = PI * R ** 2
# # Perimetro = 2 * PI * R

# radio = float(input("Ingresa el radio del circulo\n"))
# area = math.pi * (radio ** 2)
# perimetro = 2 * math.pi * radio
# print(f"El área del círculo es: {area}")
# print(f"El perímetro del círculo es: {perimetro}")
# # ----------------------------

# # Actividad N° 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

# segundos = int(input("Ingresa una cantidad de segundos a convertir a horas\n"))
# horas = float(segundos / 3600)
# print(f"{segundos} segundos equivalen a {horas:.2f} horas.")
# # ----------------------------

# # Actividad N° 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

# numero = int(input("Ingresa un número para ver su tabla de multiplicar\n"))
# print(f"Tabla de multiplicar del {numero}:")
# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")
# print("\n\n")
# # ----------------------------

# #Actividad N° 7:Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

# while True:
#     try:
#         num1 = int(input("Ingresa el primer número entero distinto de 0\n"))
#         num2 = int(input("Ingresa el segundo número entero distinto de 0\n"))
#         if num2 != 0 and num1 != 0:
#             break
#     except ValueError:
#         print("Los números deben ser entero y distinto de 0. Ingresa otro número.")
# print(f"\nResultados:")
# print(f"Suma: {num1 + num2}")
# print(f"Resta: {num1 - num2}")
# print(f"Multiplicación: {num1 * num2}")
# print(f"División: {num1 / num2}")
# # ----------------------------

# # Actividad N° 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

# altura = float(input("Ingresa tu altura en metros\n"))
# peso = float(input("Ingresa tu peso en kilogramos\n"))
# imc = peso / (altura ** 2)
# print(f"Tu índice de masa corporal es: {imc:.2f}")
# # ----------------------------

# # Actividad N° 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit

# celsius = float(input("Ingresa una temperatura en grados Celsius\n"))
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")
# # ----------------------------

# # Actividad N° 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

# num1 = float(input("Ingresa el primer número\n"))
# num2 = float(input("Ingresa el segundo número\n"))  
# num3 = float(input("Ingresa el tercer número\n"))
# promedio = (num1 + num2 + num3) / 3
# print(f"El promedio de los tres números es: {promedio:.2f}")
# # ----------------------------  

a = 10
b = 3.0
c = (10*30.0)
d = a +b

print(c)
print(d)