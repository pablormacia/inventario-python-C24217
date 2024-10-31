# Inventario
inventario = []

# Funciones
def mostrar_menu_principal():
    print("")
    print("Menú de gestión de productos: ")
    print("")
    print("1. Alta de productos nuevos")
    print("2. Consulta de datos de productos")
    print("3. Modificar la cantidad en stock de productos")
    print("4. Dar de baja productos")
    print("5. Listado completo")
    print("6. Lista de productos con bajo stock")
    print("7. Salir")
    print("")


def mostrar_inventario(inventario):
    print("")
    print("INVENTARIO:")
    if (len(inventario) == 0):
        print("El innventario está vacío")
    else:
        i = 0
        print("")
        print(f"PRODUCTO\tPRECIO\t\tSTOCK")
        while i < len(inventario):
            print(f"{inventario[i][0]}\t\t${
                  inventario[i][1]}\t\t{inventario[i][2]}")
            i += 1
        print("")

def preguntar_seguir():
    respuesta = input("¿Reintentar? s/n: ")
    while (respuesta!="n" and respuesta!="s"):
        respuesta = input("¿Reintentar? s/n: ")
    return respuesta

# Solicitar la selección de una opción
mostrar_menu_principal()
opcion = input("Por favor seleccione una opción (1-7): ")
print("")

# Validaciones

def es_float_valido(dato):
    try:
        if float(dato) >= 0:
            return True
    except:
        return False

def es_int_valido(dato):
    return dato.isdigit()


def esta_en_inventario(inventario, nombre):
    # Inventario esperado : [[nombre,precio,stock], [nombre,precio,stock],...]
    if (len(inventario) == 0):
        return False
    indice = 0
    while (indice < len(inventario)):
        if inventario[indice][0] == nombre:
            return True
        indice += 1
    return False

#Ejecución del programa
while (opcion != "7"):
    seguir = "s"
    if (opcion == "1"):
        print("AGREGAR PRODUCTO:")
        while seguir == "s":
            producto = []

            while True:
                nombre = input("Indicá el nombre del producto: ")
                if nombre == "":
                    print("El nombre no puede estar vacío")
                    seguir=preguntar_seguir()
                    if seguir == "n":
                        break
                elif esta_en_inventario(inventario, nombre):
                    print("El producto ya está en el inventario")
                    seguir=preguntar_seguir()
                    if seguir == "n":
                        break
                else:
                    break

            if seguir == "n":
                break

            while True:
                precio = input("Indicá el precio del producto: ")
                if not (es_float_valido(precio)):
                    print("Se debe ingresar un precio válido")
                    seguir=preguntar_seguir()
                    if seguir == "n":
                        break
                else:
                    break

            while True:
                stock = input("Indicá el stock actual: ")
                if not (es_int_valido(stock)):
                    print("Se debe ingresar un stock válido")
                    seguir=preguntar_seguir()
                    if seguir == "n":
                        break
                else:
                    break

            # Agrego productos a la lista producto
            producto.append(nombre)
            producto.append(float(precio))
            producto.append(int(stock))

            # Agrego el producto al inventario
            inventario.append(producto)
            mostrar_inventario(inventario)
            seguir = input("¿Agregar otro producto? s/n: ")

    elif (opcion == "5"):
        mostrar_inventario(inventario)
    
    opcion = input("Por favor seleccione una opción (1-7): ")
