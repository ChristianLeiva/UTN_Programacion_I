import math
# # Funciones
# # 01. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
# # Definición de la función
# def imprimir_hola_mundo():
#     """Imprimir un saludo estandar en la consola."""
#     print("Hola Mundo.")
# imprimir_hola_mundo()
# # ---------------------------------------------------------------------------------------------------- # #
# # 02. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
# nombre = input("Ingrese su nombre: ")
# def saludar_usuario(nombre : str):
#     """Imprime un saludo estandar usando un parametro de entrada(str)"""
#     print(f"Hola {nombre}!")
# saludar_usuario(nombre)
# # ---------------------------------------------------------------------------------------------------- # #
# # 03. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
# # Definición de funciones
# def validar_string(mensaje):
#     """Valida que los valores ingresados sean string mediante .isapha()"""
#     valor = input(mensaje).strip()
#     while not valor.replace(" ", "").isalpha():
#         valor = input("Error: Solo se permiten letras. Ingrese nuevamente: ")
#     return valor.title()

# def valir_digito(mensaje):
#     """Valida que los valores ingresados sean string mediante .isdigit()"""
#     valor = input(mensaje)
#     while not valor.isdigit():
#         valor = input("Error: el valor ingresado no es valido. Ingrese nuevamente: ")    
#     return int(valor)

# def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str) -> str:
#     """Devuelve todos los parametros de entrada en una cadena (presentacion)"""
#     presentacion = f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."
#     return presentacion
# # Carga de parametros
# nombre = validar_string("ingrese su nombre:")
# apellido = validar_string("Ingrese su apellido:") 
# edad = valir_digito("Ingrese su edad:")
# residencia = validar_string("ingrese su residencia:")
# # Llamado de la función
# print(informacion_personal(nombre, apellido, edad, residencia))
# # ---------------------------------------------------------------------------------------------------- # #
# # 04. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
# # Definición de funciones
# def calcular_area_circulo(radio: float) -> float:
#     """Calcula el área usando la fórmula: π * radio^2"""
#     return math.pi * (radio ** 2)

# def calcular_perimetro_circulo(radio: float) -> float:
#     """Calcula el perímetro usando la fórmula: 2 * π * radio"""
#     return 2 * math.pi * radio

# def validar_radio(mensaje: str) -> float:
#     """Valida que se ingrese un número positivo"""
#     entrada = input(mensaje).replace(",", ".")

#     while not entrada.replace(".", "", 1).isdigit():
#         entrada = input("Error: valor no válido positivo: ").replace(",", ".")    
#     valor = float(entrada)
    
#     while valor <= 0:
#         print("Error: El Radio debe ser mayor a 0")
#         entrada = input("Ingrese el radio nuevamente: ").replace(",", ".")
#         if entrada.isdigit():
#             valor = float(entrada)            
#     return valor    

# # # Carga de parametros
# radio_usuario = validar_radio("Ingrese el radio del circulo: ")
# area = calcular_area_circulo(radio_usuario)
# perimetro = calcular_perimetro_circulo(radio_usuario)

# print(f"\nResultados para un radio de {radio_usuario}:")
# print(f"Área: {area:.2f}")
# print(f"Perímetro: {perimetro:.2f}")
# # ---------------------------------------------------------------------------------------------------- # #
# # 05. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
# # Definición de la Función
# def segundos_a_horas(mensaje) -> str:
#     """Valida que se ingresen solo numeros mediante isdigit() y calcula los minutos"""
#     entrada = input(mensaje)
#     while not entrada.isdigit():
#         entrada = input("Error: valor invalido. Ingrese nuevamente: ")
#     segundos = int(entrada)        
#     minutos = segundos/60
#     return f"Los {entrada} segundos ingresado, equivales a {(minutos):.2f} minutos"

# print(segundos_a_horas("Ingrese los segundos a convertir: "))
# # ---------------------------------------------------------------------------------------------------- # #
# # 06. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
# # Definición de Funciones
# def tabla_multiplicar(msj):
#     """Valida que se ingresen numeros enteros y posteriormente hace la tabla de multiplicar del 1 a 10"""
#     num = input(msj)
#     while not num.isdigit():
#         num = input("Error: valor invalido. Ingrese nuevamente: ")
#     num = int(num)
#     print(f"*** Tabla de multiplicar de {num} ***")
#     for i in range(1,11):
#         print(f"{num} * {i} = {num * i}")

# print(tabla_multiplicar("Ingrese un número: "))
# # ---------------------------------------------------------------------------------------------------- # #
# # 07. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.    
# def es_numero_valido(mensaje):
#     entrada = input(mensaje).strip()    
#     """Valida que el valor ingresado sea un número y que permita valores negativos"""
#     while not (entrada.isdigit() or (entrada.startswith("-") and entrada[1:].isdigit())):
#         entrada = input("Error: valor invalido. Ingrese nuevamente: ").strip()    
#     return int(entrada)

# def suma(num1: int, num2: int) -> int:
#     """Suma de los parametros de entrada"""
#     return (num1 + num2)
# def resta(num1: int, num2: int) -> int:
#     """Resta de los parametros de entrada"""
#     return (num1 - num2)
# def multiplicacion(num1: int, num2: int) -> int:
#     return (num1 * num2)
# def division(num1: int, num2: int) -> float:
#     return (num1 / num2)

# num1 = es_numero_valido("Ingrese el primer número: ")
# num2 = es_numero_valido("Ingrese el segundo número: ")

# print(f"La suma de {num1} + {num2} = {suma(num1, num2)}")
# print(f"La resta de {num1} - {num2} = {resta(num1, num2)}")
# print(f"La multiplicación de {num1} * {num2} = {multiplicacion(num1, num2)}")
# print(f"La división de {num1} / {num2} = {division(num1, num2)}")
# # ---------------------------------------------------------------------------------------------------- # #
# # 08. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
# def calcular_imc(altura, peso):
#     print({altura, peso})
#     imc = peso / (altura ** 2)
#     return round(imc, 2)

# def validar_datos_entrada(msj):
#     valor = input(msj)
#     while not valor.replace(".", "", 1).isdigit():
#         valor = input("Erro: valor invalido. Ingrese nuevamente: ")
#     return float(valor)

# altura = validar_datos_entrada("Ingrese su altura: ")/100
# peso = validar_datos_entrada("Ingrese su peso: ")

# print(f"Su indice de masa corporal (IMC) es de {calcular_imc(altura, peso)}")
# # ---------------------------------------------------------------------------------------------------- # #
# # 09. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenhei. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
# def celsius_a_fahrenheit(celsius):
#     farenheit = (celsius*(9/5))+32
#     return farenheit

# def valida_temperatura(mensaje):
#     """Valida que el valor ingresado sea un número y que permita valores negativos"""
#     entrada = input(mensaje).strip()    
#     while not (entrada.isdigit() or (entrada.startswith("-") and entrada[1:].isdigit())):
#         entrada = input("Error: valor invalido. Ingrese nuevamente: ").strip()    
#     return float(entrada)

# celsius = valida_temperatura("Ingrese su temperatura en °Celsius: ")
# print(f"La temperatura en {celsius}°C = {celsius_a_fahrenheit(celsius)}°F")
# # ---------------------------------------------------------------------------------------------------- # #
# # 10. Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
# def es_numero_valido():
#     """Valida que el valor ingresado sea un número y que permita valores negativos y los almacena en un array"""
#     numeros = []
#     for i in range(3):
#         entrada = input(f"Ingrese el número {i+1} de 3: ").strip()    
#         while not (entrada.isdigit() or (entrada.startswith("-") and entrada[1:].isdigit())):
#             entrada = input("Error: valor invalido. Ingrese nuevamente: ").strip()
#         numeros.append(int(entrada))    
#     return numeros

# def calcular_promedio(numeros: list):
#     sumador = 0
#     for n in numeros:
#         sumador += n
#     prom = sumador/(len(numeros))
#     return prom

# lista_numeros = es_numero_valido()
# print(f"El promedio es: {calcular_promedio(lista_numeros)}")

