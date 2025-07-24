lista_compras = ["pan", "leche", "huevo", "harina"]

def mostrar_lista():
    print(f"Lista de compras actual:", lista_compras)

def agregar_producto():
    producto = input("Ingrese el producto a agregar: ").strip()
    if producto in lista_compras:
        print(f"El producto '{producto}' ya está en la lista.")
    elif producto:
        lista_compras.append(producto)
        print(f"Producto '{producto}' agregado a la lista.")
    else:
        print("El nombre del producto no puede estar vacío.")

def eliminar_producto():
    producto = input("Ingrese el producto a eliminar: ").strip()
    if producto in lista_compras:
        lista_compras.remove(producto)
        print(f"Producto '{producto}' eliminado de la lista.")
    else:
        print(f"El producto '{producto}' no está en la lista.")

while True:
    print("\nMenú:")
    print("1. Mostrar lista")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ").strip()
    if opcion == "1":
        mostrar_lista()
    elif opcion == "2":
        agregar_producto()
        mostrar_lista()
    elif opcion == "3":
        eliminar_producto()
        mostrar_lista()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")