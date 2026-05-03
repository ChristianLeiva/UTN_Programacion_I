# # Trabajo Practico N° 7: Estructura de Datos Complejas
def validar_nombre(msj: str) -> str:
    nombre = input(msj).capitalize()
    while not nombre.isalpha():
        nombre = input("Error: El nombre es invalido. Ingrese nuevamente: ")
    return nombre

def validar_numero(msj : str) -> int:
    numero = input(msj)
    while not numero.isdigit():
        numero = input("Error: El número es invalido. Ingrese nuevamente: ")
    return int(numero)

# precios_frutas = {
#     'Banana': 1200, 
#     'Ananá': 2500, 
#     'Melón': 3000, 
#     'Uva': 1450
# }

# # Agregar frutas al diccinario:
# precios_frutas["Naranja"] = 1200
# precios_frutas["Manzana"] = 1500
# precios_frutas["Pera"] = 2300
# print(precios_frutas)
# print("--------------------------")

# # Siguendo con el diccionario precio_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguentes frutas
# precios_frutas["Banana"] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800
# print(precios_frutas)
# print("--------------------------")

# # Siguendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga unicamente las frutas sin los precios.
# frutas = list(precios_frutas.keys())
# print(frutas)
# print("--------------------------")

# # Escribí un programa que permita almacenar y consultar números telefónicos.
# # Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# #uego, pedí un nombre y mostrale el número asociado, si existe.
# agenda = dict()

# print("** Creandno Agenda **")
# for c in range(5):
#     """Loop para cargar la agenda"""
#     nombre = validar_nombre(f"Ingrese el nombre del contacto {c+1}: ")
#     telefono = validar_numero(f"Ingrese el telefono del contacto {nombre}: ")
#     agenda[nombre] = telefono
#     print("Contacto Agendado...")

# print("** Busqueda de contacto **")
# nombre = validar_nombre("Ingrese el nombre de la contacto que busca: ")

# if nombre in agenda:
#     print("Contacto encontrado:")
#     print(f"{nombre}: {agenda[nombre]}")
# else:
#     print(f"El contacto {nombre} no existe en la agenda")

# # Solicitar una frase e imprime:
# # las palabras únicas (usando un set).
# # Un diccionario con la cantidad de veces que aparece cada palabra
# frase = input("Ingrese una frase: ")
# # Con split dividimos la frase por espacios y se gurda en una lista
# lista_frase = frase.split(" ")
# palabras_unicas = set(lista_frase)
# print("** Palabras Únicas **")
# print(palabras_unicas)

# repeticiones = {}
# for p in lista_frase:
#     if p in repeticiones:
#         repeticiones[p] +=1
#     else:
#         repeticiones[p] = 1

# print("** Repeticiones por palabra **")
# print(repeticiones)

# # Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego mostrá el promedio de cada alumno
# alumnos = {}
# # Carga de Datos
# for a in range(3):
#     notas = []
#     nombre = validar_nombre(f"Ingresa el nombre del alumno {a+1}: ")
#     for n in range(3):
#         nota = validar_numero(f"Ingresa la nota {n+1} del alumno {nombre}: ")
#         notas.append(nota)
#     alumnos[nombre] = tuple(notas)
# print(alumnos)
# # promedio de notas
# for nombre, notas in alumnos.items():
#     prom = sum(notas) / len(notas)
#     print(f"El promedio de {nombre} es: {prom}")

# # Se recibe el registro diario de asistencia a una capacitación en forma de lista. En dicha lista pueden aparecer nombres repetidos, ya que una misma persona pudo haber asistido en más de una jornada.
# # Mostrá la lista original de asistencias.
# # Generá un conjunto (set) a partir de la lista y mostrar los empleados que asistieron al menos una vez (sin repetir nombres).
# # Indicá cuántas veces asistió cada empleado a la capacitación.
# asistencia_curso = {}
# asistencia = ["Ana", "Luis", "Ana", "Maria", "Luis", "Pedro", "Ana"]
# print("** Lista Original de asistencias **")
# print(asistencia)
# asistencia_sin_repeticiones = set(asistencia)
# print("** Asistencia sin repeticiones **")
# print(asistencia_sin_repeticiones)
# print("** Asistencia por empleados **")
# for e in asistencia:
#     if e in asistencia_curso:
#         asistencia_curso[e] += 1
#     else:
#         asistencia_curso[e] = 1
# print(asistencia_curso)

#Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.
# productos = {
#     "Teclado" : 2,
#     "Mouse" : 3
# }
# print("Bienveido al sistema de stock")
# while True:
#     opcion_ingresada = validar_numero("Ingrese la opción deseada:\n1- Consultar Stock.\n2- Agregar Stock.\n3- Agregar Producto Nuevo.\n4- Salir.\n")
#     if opcion_ingresada == 1:
#         print("Consulta de Stock")
#         print(productos)
#         print("\n")
#     elif opcion_ingresada == 2:
#         print("Agregar Stock")
#         producto_nombre = validar_nombre("Agregar el nombre del producto para actualizar stock: ")
#         if producto_nombre in productos:
#             stock_nuevo = validar_numero("Ingrese el stock a actualizar: ")
#             productos[producto_nombre] = stock_nuevo
#             print("Lista de productos actualizada.")
#             print(productos)
#             print("\n")
#         else:
#             print("Error: Producto no encontrado.")        
#             print("\n")
#     elif opcion_ingresada == 3:
#         print("Agregar producto nuevo")
#         producto_nuevo = validar_nombre("Ingrese el nombre del producto a agregar: ")
#         stock_producto_nuevo = validar_numero(f"Ingrese el stock del producto {producto_nuevo}: ")
#         productos[producto_nuevo] = stock_producto_nuevo
#         print("Lista de productos actualizada.")
#         print(productos)
#         print("\n")
#     elif opcion_ingresada == 4:
#         print("Saliendo...")
#         break
#     else:
#         print("Error: opción Incorrecta. Ingrese nuevamente.")
#         continue

# # Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Permití consultar qué actividad hay en cierto día y hora.
# agenda = {}
# print("** Agenda **")
# while True:
#     opcion_ingresada = validar_numero("Ingrese la opción deseada\n1- Ver agenda completa.\n2- Consultar Agenda.\n3- Agregar Evento.\n4- Salir.\n")
#     if opcion_ingresada == 1:
#         if len(agenda) == 0:
#             print("Agenda Vacía. No existen eventos.\n")
#             continue
#         else:
#             print(agenda)
#     elif opcion_ingresada == 2:
#         print("** Buscar Evento **")
#         dia_busqueda = validar_nombre("Ingrese el día que desea consultar: ")
#         hora_busqueda = validar_numero("Ingrese la hora (ej 1230): ")

#         hora_str = str(hora_busqueda).zfill(4)
#         hora_formateada = f"{hora_str[:2]}:{hora_str[2:]} hs"

#         clave_busqueda = (dia_busqueda, hora_formateada)

#         if clave_busqueda in agenda:
#             print(f"Evento encontrado!")
#             print(f"Actividad: {agenda[clave_busqueda]}")
#         else:
#             print(f"No hay ninguna actividad programada para el {dia_busqueda} a las {hora_formateada}.")
#     elif opcion_ingresada == 3:
#         print("** Agregar Evento. **")
#         dia = validar_nombre("Ingrese el día del evento: ")
#         hora = validar_numero("Indique la hora del evento(sin espacios ni doble punto ej 1230): ")
#         evento_nombre = input("Ingrese el nombre del evento: ")

#         hora_str = str(hora)
#         hora_formateada = f"{hora_str[:2]}:{hora_str[2:]} hs"
#         agenda[(dia, hora_formateada)] = evento_nombre
#         print("Evento agregado exitosamente.")
#     elif opcion_ingresada == 4:
#         print("Saliendo...")
#         break
#     else:
#         print("Error: Opción Invalida. Ingrese nuevamente.")
#         continue

# Dado un diccionario que mapea nombres de países con sus capitales, construí uno nuevo donde las capitales sean las claves y los paises los valores
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais
print("Diccionario invertido:")
print(capitales_paises)