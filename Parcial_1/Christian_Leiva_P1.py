# # Sistema de Control de Inventario
# # Contexto del Problema
# # Una ferretería local necesita digitalizar el control de sus productos para evitar pérdidas de stock. Actualmente, manejan sus datos de forma manual y requieren un programa que permita gestionar las herramientas a la venta y sus unidades disponibles en tiempo real.
# # Funcionalidades del Menú
# # 1. Carga Inicial de Herramientas: Registrar los nombres de las herramientas que se pondrán a la venta. Se debe preguntar al usuario la cantidad de herramientas a cargar y se debe usar una estructura pertinente. En caso de nombre vacío o duplicado se debe seguir pidiendo hasta que sea correcto respetando la cantidad de herramientas que el usuario indicó antes de la carga.
# # 2. Carga de Existencias: Ingresar la cantidad de unidades para cada herramienta registrada previamente, respetando el orden de ingreso. Cuando el usuario ingresa existencias, el sistema debe mostrar por pantalla el nombre de la herramienta.
# # 3. Visualización de Inventario: Mostrar el listado completo de herramientas junto a su stock actual.
# # 4. Consulta de Stock (existencias): Buscar una herramienta por su nombre y mostrar cuántas unidades hay disponibles.
# # 5. Reporte de Agotados: Listar únicamente aquellos productos cuyo stock sea igual a cero.
# # 6. Alta de Nuevo Producto: Permitir agregar solo una nueva herramienta al final de las listas con su stock inicial. En caso de nombre vacío, nombre duplicado o valor de existencia negativo se debe volver al menú principal mostrando por pantalla el motivo
# # 7. Actualización de Stock (Venta/Ingreso):
# # - Venta: Disminuir el stock tras validar que hay unidades suficientes.
# # - Ingreso: Aumentar el stock por reposición de mercadería.
# # 8. Salir: Finalizar la ejecución del sistema.
# # Criterios de Validación (Robustez)
# # El sistema debe ser "a prueba de errores" comunes:
# # - No permitir nombres de herramientas vacíos ni duplicados.
# # - No permitir ingresar existencias (opción 2 del menú) sin tener nombres de herramientas cargadas (opción 1)
# # - Validar que las existencias ingresadas sean números enteros positivos o cero.
# # - Impedir ventas que superen el stock disponible (no se permiten saldos negativos).
# # - Informar mediante un mensaje claro si se intenta operar sobre una herramienta que no existe en el catálogo.