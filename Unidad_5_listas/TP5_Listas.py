import random
# # Ejercicio 1
# # Crear una lista con las notas de 10 estudiantes.
# # Mostrar la lista completa.
# # Calcular y mostrar el promedio.
# # Indicar la nota más alta y la más baja.

# notas = [10, 9, 8, 7, 9, 6, 5, 3, 4, 8]
# # mostrar lista y sumar
# suma = 0
# for nota in notas:
#     print(nota)
#     suma += nota
# # promedio
# prom = suma / len(notas)
# print(f"El promedio de todas las notas es: {prom}")
# # min y max
# nota_min = min(notas)
# nota_max = max(notas)
# print(f"La nota más baja es: {nota_min}, y la mas alta es: {nota_max}")
# # ----------------------------------------------------------------------

# # Ejercicio 2
# # Pedir al usuario que cargue 5 productos en una lista
# # Mostrar la lista ordenada alfabeticamente.
# # Preguntar al uusuario qué producto desea eliminar y actualizar la lista
# productos = []
# # Cargamos la lista
# for p in range(5):
#     p_nombre = input("Ingrese el nombre del producto para agregar a la lista.\n").strip().lower()
#     while (not p_nombre.isalpha()):
#         print("Error: Nombre de producto invalido.")
#         p_nombre = input("Ingrese el nombre del producto para agregar a la lista.\n").strip().lower()
#     productos.append(p_nombre)
# # Ordenamos alfabeticamente la lista
# productos_ordenados = sorted(productos)
# # Mostramos la lista
# for p in range(len(productos_ordenados)):
#     print(f"{p + 1} - {productos_ordenados[p].capitalize()}")
# # Preguntamos al usuario si quiere eliminar o no un producto de la lista
# respuesta = input("¿Desea eliminar un producto de la lista? S/N.\n").strip().lower()
# while respuesta not in ["s", "n"]:
#     print("Error: respusta no valida")
#     respuesta = input("¿Desea eliminar un producto de la lista? S/N.\n").strip().lower()
# if respuesta == 's':
#     while len(productos_ordenados) > 0:
#         p_eliminar = input("¿Qué producto desea eliminar? 'fin' para salir.\n").strip().lower()
#         if p_eliminar == 'fin':
#             print("Saliendo del programa...")
#             break
#         if p_eliminar in productos_ordenados:
#             productos_ordenados.remove(p_eliminar)
#             print(f"El producto:{p_eliminar.capitalize()} se eliminó de la lista.")
#         else:
#             print(f"El producto: {p_eliminar.capitalize()} no existe en la lista.")
# if(len(productos_ordenados) == 0):
#     print("\nLa lista está vacía. No hay más productos para eliminar.")
# else:
#     print("\nLista de productos definitivas:")
#     for p in range(len(productos_ordenados)):
#         print(f"{p + 1} - {productos_ordenados[p].capitalize()}")
# # ----------------------------------------------------------------------

# # Ejercicio 3
# # Generar una lista con 15 números enteros al azar entre 1 y 100.
# # Crear una lista con los pares y otros con los impares
# # Mostrar cuantos números tiene cada lista
# numeros = []
# lista_pares = []
# lista_impares = []
# # Cargamos la lista
# for n in range(15):
#     numeros.append(random.randint(1, 100))
# # Mostramos la lista
# print("--- Lista Original ---")
# for n in numeros:
#     print(f"{n}", end=" ")
# print("\n")
# # Dividimos pares e impares
# for i in numeros:
#     if i % 2 == 0:
#         lista_pares.append(i)
#     else:
#         lista_impares.append(i)
# # Mostramos los Pares
# print(f"PARES: {len(lista_pares)} números:")
# for np in lista_pares:
#     print(np, end="  ") 
# print("\n")
# # Mostramos los Impares
# print(f"IMPARES: {len(lista_impares)} números:")
# for ni in lista_impares:
#     print(ni, end="  ")
# print("\n")
# # ----------------------------------------------------------------------

# # Ejercicio 4
# # Dada una lista con valores repetidos
# # Crear una nueva lista sin valores repetidos
# numeros = []
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# # Recorremos la lista y agreamos a la nueva lista
# for d in datos:
#     if(d not in numeros):
#         numeros.append(d)
# # Mostramos la nueva lista
# print("Lista sin elementos repetidos:")
# for n in numeros:
#     print(f"{n}", end=" ")
# # ----------------------------------------------------------------------

# # Ejercicio 5
# # Crear una lista con los nombres de 8 estudiantes presentes en clase
# # Preguntar usuario si quiere agregar un nuevo estudiante o eliminar uno existe
# # Mostar la lista final actualizada
# alumnos = []
# # Cargamos la lista con 8 nombres de alumnos
# for a in range(8):
#     nombre = input("Por favor, ingrese el nombre del alumno:\n").strip().capitalize()
#     # Validamos que se ingrese nombres sin números
#     while not nombre.isalpha():
#         print("Error: el nombre ingresado no es valido.")
#         nombre = input("Por favor, ingrese el nombre del alumno:\n").strip().capitalize()
#     alumnos.append(nombre)
# while (len(alumnos) > 0):
#     opcion = input("¿Editar Lista?:\n1) Agregar.\n2) Eliminar.\n3) Salir.\n")
#     while not opcion.isdigit():
#         print("Error: el valor ingregado no es valido.")
#         opcion = input("¿Editar Lista?:\n1) Agregar.\n2) Eliminar.\n3) Salir.\n")
#     opcion = int(opcion)
#     if opcion == 3:
#         break;
#     nombre = input("Por favor, ingrese el nombre del alumno:\n").strip().capitalize()
#     while not nombre.isalpha():
#         print("Error: el nombre ingresado no es valido.")
#         nombre = input("Por favor, ingrese el nombre del alumno:\n").strip().capitalize()
#     if opcion == 1:
#         alumnos.append(nombre)
#     elif opcion == 2:
#         if(nombre in alumnos):
#             alumnos.remove(nombre)
#             print(f"El alumno {nombre}, fue eliminado de la lista.")
#         else:
#             print(f"El alumno {nombre}, no existe en la lista.")        
# if(len(alumnos) <= 0):
#     print("\nLa lista está vacía. No hay más alumnos para eliminar.")
# print("*** Lista de alumnos ***")
# for a in range(len(alumnos)):
#     print(f"{a+1} - {alumnos[a]}")
# # ----------------------------------------------------------------------

# # Ejercicio 6
# # Dada una lista con 7 números, rotar todos los números a la derecha (el útimo pasa a ser el primero)
# numeros = []
# for i in range(7):
#     numeros.append(random.randint(1 , 100))
# print("\n*** Lista Original ***")
# print(numeros)
# ultimo = numeros[-1]
# for n in range(len(numeros)-1, 0, -1):
#     numeros[n] = numeros[n - 1]
# numeros[0] = ultimo
# print("\n*** Lista editada ***")
# print(numeros)
# # ----------------------------------------------------------------------

# # Ejercicio 7
# # Crear una matriz anidada 7*2 con las temperaturas minimas y maximas de una semana
# # Calcular promedio de las minimas y maximas
# # Mostrar en que día se registro la mayor amplitud termica
# temperaturas = [
#     [10, 25],  # Domingo
#     [12, 28],  # Lunes
#     [8, 22],   # Martes
#     [9, 24],   # Miercoles
#     [11, 27],  # Jueves
#     [7, 20],   # Viernes
#     [13, 30]   # Sabado
# ]
# suma_temp_baja = 0
# suma_temp_alta = 0
# mayor_aplitud = 0
# dia_mayor_aplitud = 0
# for i in range(7):
#     minima = temperaturas[i][0]
#     maxima = temperaturas[i][1]

#     suma_temp_baja += minima
#     suma_temp_alta += maxima

#     amplitud = maxima - minima

#     if amplitud > mayor_aplitud:
#         mayor_aplitud = amplitud
#         dia_mayor_aplitud = i
# prom_bajas = (suma_temp_baja / 7)
# prom_altas = (suma_temp_alta / 7)
# print(f"Promedio mínimas: {(prom_bajas):.2f}")
# print(f"Promedio máximas: {(prom_altas):.2f}")
# print(f"Mayor amplitud térmica: {mayor_aplitud} en el día {dia_mayor_aplitud + 1}")
# # ----------------------------------------------------------------------

# # Ejercicio 8
# # Crear una matriz con las notas de 5 estudiantes en 3 materias.
# # Mostrar el promedio de cada estudiante.
# # Mostrar el promedio de cada materia.
# notas_alumno = [
#     ["Alejandro"],
#     ["Osvaldo"], 
#     ["Franco"],
#     ["Andrea"],
#     ["Julio"]
# ]
# prom_alumno = 0
# suma_prom_alumno = 0
# suma_prom_materia1 = 0
# suma_prom_materia2 = 0
# suma_prom_materia3 = 0
# # cargar matriz con notas
# for n in range(len(notas_alumno)):
#     for i in range(3):
#         notas_alumno[n].append(random.randint(1, 10))
# print("*** Lista de notas ***")
# for n in range(len(notas_alumno)):
#     print(notas_alumno[n])
# print("\n*** Promedio de alumnos ***")
# for alumno in range(len(notas_alumno)):
#     suma_prom_alumno = notas_alumno[alumno][1] + notas_alumno[alumno][2] + notas_alumno[alumno][3]
#     print(f"El promedio del alumno: {notas_alumno[alumno][0]} es de {(suma_prom_alumno/3):.2f}")
#     suma_prom_materia1 += notas_alumno[alumno][1]
#     suma_prom_materia2 += notas_alumno[alumno][2]
#     suma_prom_materia3 += notas_alumno[alumno][3]

# print("\n*** Promedio por materias ***")
# print(f"El promedio de la materia 1 es: {(suma_prom_materia1/len(notas_alumno)):.2f}")
# print(f"El promedio de la materia 2 es: {(suma_prom_materia2/len(notas_alumno)):.2f}")
# print(f"El promedio de la materia 3 es: {(suma_prom_materia3/len(notas_alumno)):.2f}")
# # ----------------------------------------------------------------------

# # Ejercicio 9
# # Representar un tablero de TA - TE - TI como una lista (3 X 3).
# # Iniciarlo con guiones "_" representando casillas vacias
# # Mostrar el tablero despues de cada jugada
# Ta-Te-Ti
# tablero = [
#     ["__", "__", "__"],
#     ["__", "__", "__"],
#     ["__", "__", "__"],
# ]
# jugador = "X"
# ganador = False
# movimientos = 0
# ganador_jugador = ""
# while not ganador and movimientos < 9:
#     # Mostrar tablero
#     print("\nTablero:")
#     for fila_tablero in tablero:
#         print(fila_tablero)
#     fila = input("Elija la fila (1-3): ")
#     while not fila.isdigit() or fila not in ["1", "2", "3"]:
#         print("Error: número de fila inválido")
#         fila = input("Elija la fila (1-3): ")
#     fila = int(fila) - 1
#     columna = input("Elija la columna (1-3): ")
#     while not columna.isdigit() or columna not in ["1", "2", "3"]:
#         print("Error: número de columna inválido")
#         columna = input("Elija la columna (1-3): ")
#     columna = int(columna) - 1
#     # Verificar casillero
#     if tablero[fila][columna] == "__":
#         tablero[fila][columna] = jugador
#         print("Jugada aceptada.\n")
#         movimientos += 1
#     else:
#         print("Casillero ocupado, intente de nuevo.")
#         continue
#     # Verificar filas
#     for f in range(3):
#         if tablero[f][0] != "__" and tablero[f][0] == tablero[f][1] == tablero[f][2]:
#             ganador = True
#     # Verificar columnas
#     for c in range(3):
#         if tablero[0][c] != "__" and tablero[0][c] == tablero[1][c] == tablero[2][c]:
#             ganador = True
#     # Verificar diagonales
#     if tablero[0][0] != "__" and tablero[0][0] == tablero[1][1] == tablero[2][2]:
#         ganador = True
#     if tablero[0][2] != "__" and tablero[0][2] == tablero[1][1] == tablero[2][0]:
#         ganador = True
#     # Guardar ganador antes de cambiar turno
#     if ganador:
#         ganador_jugador = jugador
#         break
#     # Cambiar jugador
#     if jugador == 'X':
#         jugador = 'O'
#     else:
#         jugador = 'X'
# # Resultado final
# print("\nTablero final:")
# for fila_tablero in tablero:
#     print(fila_tablero)
# if ganador:
#     print(f"\nEl jugador {ganador_jugador} ha ganado.")
# else:
#     print("\nEs un empate!")
# # ----------------------------------------------------------------------
# Ejercicio 10
# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4*7.
# Mostrar el total vendido por cada producto.
# Mostrar el día con mayores ventas totales
# Indicar cual fue el producto más vendido de la semana
# dias = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
# ventas = [
#     ["prod 1"],
#     ["prod 2"],
#     ["prod 3"],
#     ["prod 4"],
# ]
# total_prod_1 = 0
# total_prod_2 = 0
# total_prod_3 = 0
# total_prod_4 = 0
# mayor_venta = 0
# dia_venta = 0
# suma = 0
# # Carga de matriz con numeros aleatorios de 1,20
# for i in range(len(ventas)):
#     for j in range(7):
#         ventas[i].append(random.randint(1, 20))
# # # Mostramos la lista ventas
# print("*** Lista de Ventas ***")
# for v in range(len(ventas)):
#     print(ventas[v])
# # suma total de ventas por producto
# print("\n*** Total de ventas por producto ***")
# for f in range(len(ventas)):
#     for c in range(len(ventas[f])):
#         if(ventas[f][c] == "prod 1"):
#             total_prod_1 = sum(ventas[f][1:])
#             print(f"El total de ventas del {ventas[f][0]} es de {total_prod_1}")
#         if(ventas[f][c] == "prod 2"):
#             total_prod_2 = sum(ventas[f][1:])
#             print(f"El total de ventas del {ventas[f][0]} es de {total_prod_2}")
#         if(ventas[f][c] == "prod 3"):
#             total_prod_3 = sum(ventas[f][1:])
#             print(f"El total de ventas del {ventas[f][0]} es de {total_prod_3}")
#         if(ventas[f][c] == "prod 4"):
#             total_prod_4 = sum(ventas[f][1:])
#             print(f"El total de ventas del {ventas[f][0]} es de {total_prod_4}")
# print("\n*** Día con mayor venta ***" )
# for c in range(1, len(ventas[0])):
#     ventas_dia = 0    
#     for f in range(len(ventas)):
#         ventas_dia += ventas[f][c]    
#     if ventas_dia > mayor_venta:
#         mayor_venta = ventas_dia
#         dia_venta = c
# print(f"El día con mayor venta fue {dias[dia_venta]}")
# print("\n*** Producto más vendido ***" )
# if total_prod_1 > total_prod_2 and total_prod_1 > total_prod_3 and total_prod_1 > total_prod_4:
#     print("El producto más vendido es el 1")
# elif total_prod_2 > total_prod_1 and total_prod_2 > total_prod_3 and total_prod_2 > total_prod_4:
#     print("El producto más vendido es el 2")
# elif total_prod_3 > total_prod_1 and total_prod_3 > total_prod_2 and total_prod_3 > total_prod_4:
#     print("El producto más vendido es el 3")
# else:
#     print("El producto más vendido es el 4")

# # ----------------------------------------------------------------------
# # Ejercicio 12
# # 
# # 
# # ----------------------------------------------------------------------
# # Ejercicio 13
# # 
# # 
# # ----------------------------------------------------------------------
# # Ejercicio 
# # 
# # 
# # ----------------------------------------------------------------------
# # Ejercicio 
# # 
# # 