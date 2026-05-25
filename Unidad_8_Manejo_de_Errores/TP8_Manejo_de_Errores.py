## Ejercicio 1
## Identifica los errores del código usando comentarios (#) en las líneas afectadas. Indica el tipo de error y una breve explicación de por qué ocurre.
# a = 10
# b = input("Introduce un número: ")
# result = a / b  
# # Error: valueError. 'b' es un string (input siempre devuelve texto) y no se puede dividir un entero por un string. 
# # Error: ZeroDivisionError si el usuario ingresa '0' después de convertirlo.
# print(f"Resultado: {result}")

# numbers = [1, 2, 3]
# print(numbers[5])  
# # Error: IndexError. Se intenta acceder al índice 5, pero la lista solo tiene elementos hasta el índice 2 (los índices son 0, 1 y 2).

##--------------------------------------------------------------------------------------------------------------------------------------------------------##
## Ejercicio 2
## Utilizando el código del ejercicio 1, arreglar los errores para que la ejecución del programa sea correcta sin necesidad de usar excepciones.
# a = 10
# while True:
#     b = input("Introduce un número: ")
#     if b == "0":
#         print("Error: No se puede ingresar el número 0. Intente nuevamente.")
#         continue
#     if  not b.isdigit():
#         print("Error: Caracter Invalido. Intente nuevamente.")
#         continue
#     else:
#         b = int(b)
#         break
# result = a / b
# print(result)

# numbers = [1, 2, 3]

# while True:
#     index = input("Ingrese el indice del array: ")
    
#     # .lstrip('-') elimina el signo menos de la izquierda SOLO para la validación. para ingresar valores negativos ejemplo -2
#     if not index.lstrip('-').isdigit():
#         print("Error: Caracter invalido. Intente nuevamente.")
#         continue

#     index = int(index)
   
#     if index >= len(numbers) or index < -len(numbers):
#         print("Error: El número ingresado supera los límites del arreglo. Intente nuevamente.")
#         continue
    
#     break

# print(f"Elemento encontrado: {numbers[index]}")

##--------------------------------------------------------------------------------------------------------------------------------------------------------##
## Ejercicio 3
## Utilizando el código del ejercicio 1, mantener el código con los errores originales e incluir bloques try-except para que la ejecución del programa no se frene al encontrar los errores.

# a = 10
# try:
#     b = int(input("Introduce un número: "))
#     result = a / b
#     print(f"Resultado: {result}")
# except ValueError:
#     print("Error: Caracter Invalido. Intente nuevamente. ")
# except ZeroDivisionError:
#     print("Error: No se puede dividir por 0. Intente nuevamente. ")

# try:
#     numbers = [1, 2, 3]
#     print(numbers[5])
# except IndexError:
#     print("Error: El indice ingresado, supera el limite del arreglo.")

##--------------------------------------------------------------------------------------------------------------------------------------------------------##
## Ejercicio 4
## Repetir el ejercicio 3, pero usando excepciones múltiples que hagan alusión a lostipos de errores detectados.
# a = 10
# try:
#     b = int(input("Introduce un número: "))
#     result = a / b
#     print(f"Resultado: {result}")
# except (ValueError, ZeroDivisionError):
#     print("Error: Ingrese un número distinto a 0")

##--------------------------------------------------------------------------------------------------------------------------------------------------------##
## Ejercicio 5
## Repetir el ejercicio 4, pero esta vezincluyendo bloques else y finally.
# a = 10
# try:
#     b = int(input("Introduce un número: "))
#     result = a / b
# except (ValueError, ZeroDivisionError):
#     print("Error: Ingrese un número distinto a 0")
# else:
#     print(f"Resultado: {result}")
# finally:
#     print("Fin del programa!")

# try:
#     numbers = [1, 2, 3]
#     indice = 1
#     resultado = numbers[indice]
# except IndexError:
#     print("Error: El indice ingresado, supera el limite del arreglo.")
# else:
#     print(f"El valor del arreglo en el indice {indice} es: {resultado}")
# finally:
#     print("Fin del programa!")


##--------------------------------------------------------------------------------------------------------------------------------------------------------##
## Ejercicio 6
## Escribir un programa que pida al usuario un número, y:
# Si el valor ingresado es válido, lo imprima por pantalla.
# Si el valor ingresado no es numérico, imprima por pantalla “Debe ingresar un número válido”.
# Si contiene algún otro tipo de error, imprima por pantalla “Se produjo un error inesperado” junto con el error que surgió.
# try:
#     num = int(input("Ingrese un número: "))
# except ValueError:
#     print("Error: Caracter Invalido")
# except Exception as e:
#     print(f"Se produjo un error inesperado: {type(e).__name__}")
# else:
#     print(f"El número ingresado es: {num}")
# finally:
#     print("Fin del programa!")

##--------------------------------------------------------------------------------------------------------------------------------------------------------##
## Ejercicio 7
## Repetir el ejercicio 6, pero añadiendo la posibilidad de que el usuario intente ingresar un nuevo número luego de encontrar un error.
# while True:
#     try:
#         num = int(input("Ingrese un número: "))
#         print(romper)
#     except ValueError:
#         print("Debe ingresar un número válido.")
#         continue
#     except KeyboardInterrupt:
#         print("\nPrograma cancelado por el usuario.")
#         break 
#     except Exception as e:
#         print(f"Se produjo un error inesperado: {type(e).__name__}")
#         continue
#     else:
#         print(f"El número ingresado es: {num}")
#         break
# print("Fin del programa!")