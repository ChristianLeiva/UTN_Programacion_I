# Ejercicio N° 1 - Caja del Kiosco
# Requisitos:
# 1 - Pedir el nombre del cliente (Solo letras, validar con .isalpha() en while)
# 2 - Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while)
# 3 - Por cada producto (usar for):
#     - Pedir Precio (número entero, validar .isdigit())
#     - Pedir si tiene descuento S/N (Validar con while, aceptar s o n en mayusculas/minusculas)
#     - Si tiene descuento: aplicar el 10% al precio de ese producto
# 4 - Al final mostrar:
#     - Total sin descuentos
#     - Total con descuentos
#     - Ahorro totalSinDescuentos
#     - Promedio por producto (usar float y formatear con: .2f)
# Validaciones Obligatorias
# - Sin Try/Except
# - No aceptar vacio en nombre(Si queda vacio, es error)
# - Cantidad > 0, (Si ingresa 0, volver a pedir)

totalSinDescuentos = 0
totalConDescuentos = float(0.0)
precioProducto = 0
listaProductos = ""
#Ingreso de nombre con validaciones
clienteNombre = input("Ingrese nombre del cliente: \n- ")
while (not clienteNombre.isalpha() or len(clienteNombre) == 0):
    print("Error: El nombre ingresado no es valido.")
    clienteNombre = input("Ingrese nombre del cliente: \n- ")
#Ingreso de cantidad de productos con validaciones
cantidadProductos = (input("Ingrese la cantidad de productos a comprar: \n- "))
while (not cantidadProductos.isdigit() or int(cantidadProductos) <= 0):
    print("Error: El número de productos a comprar no es valido.")
    cantidadProductos = input("Ingrese la cantidad de productos a comprar: \n- ")
cantidadProductos = int(cantidadProductos)

for producto in range(cantidadProductos):
    precioProducto = input(f"Ingrese el precio del producto {producto+1}: ")
    while (not precioProducto.isdigit() or int(precioProducto) <= 0):
        print("Error: El precio del producto ingresado no es valido.")
        precioProducto = input(f"Ingrese el precio del producto {producto+1}: \n")
    precioProducto = int(precioProducto)
    
    descuentoProducto = input("¿El producto tiene descuento? S/N: ").lower()
    while (not descuentoProducto.isalpha() or descuentoProducto not in ['s', 'n']):
        print("Error: Respuesta incorrecta.")
        descuentoProducto = input("¿El producto tiene descuento? S/N").lower()
    listaProductos += (f"Producto {producto+1}, - Precio: {precioProducto} - Descuento (S/N): {descuentoProducto}\n")

    totalSinDescuentos += precioProducto
    
    if(descuentoProducto == "s"):
        totalConDescuentos += (precioProducto * 0.9)
    else:
        totalConDescuentos += precioProducto
    
print("--------- Lista de productos ---------")
print(f"Cliente: {clienteNombre}")
print(f"Cantidad de productos: {cantidadProductos}")
print(listaProductos)
print(f"Total sin descuentos : ${totalSinDescuentos}")
print(f"Total con descuentos : ${(totalConDescuentos):.2f}")
print(f"Ahorro               : ${(totalSinDescuentos - totalConDescuentos):.2f}")
print(f"Promedio por producto: ${(totalSinDescuentos/cantidadProductos):.2f}")



