def leer_registros(nombre_fichero):
    registros = []
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
            for linea in fichero:
                campos = linea.strip().split(';')
                # Asumimos que el fichero está bien formateado, conversión directa.
                # Si hay un error aquí, será capturado por el Exception general.
                nombre = campos[0]
                edad = int(campos[1])
                salario = float(campos[2].replace(',', '.')) # Reemplazar coma por punto para la conversión a float
                nif = campos[3]
                telefono = campos[4]
                registros.append([nombre, edad, salario, nif, telefono])

        if registros:
            print(f"Se han cargado {len(registros)} registros del archivo '{nombre_fichero}'.")
        else:
            print(f"No se cargaron registros o el archivo '{nombre_fichero}' está vacío.")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_fichero}' no existe.")
    except Exception as e:
        print(f"Error al leer o procesar el archivo '{nombre_fichero}': {e}. Verifique el formato del archivo.")
    return registros

def imprimir_registros(registros):
    if not registros:
        print("No hay registros para mostrar.")
        return

    print("\nRegistros:")
    for registro in registros:
        print(f"{registro[0]}, {registro[1]}, {round(registro[2], 2)} €, {registro[3]}, {registro[4]}")

def agregar_registro(registros):
    print("\nAgregar nuevo registro:")
    nombre = input("Nombre completo: ")
    while True:
        try:
            edad_str = input("Edad: ")
            if not edad_str:
                print("La edad no puede estar vacía.")
                continue
            edad = int(edad_str)
            if edad < 0:
                print("La edad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Edad inválida. Debe ser un número entero.")

    while True:
        try:
            salario_str = input("Salario (ej: 1500.50 o 1500,50): ")
            if not salario_str:
                print("El salario no puede estar vacío.")
                continue
            salario = float(salario_str.replace(',', '.'))
            if salario < 0:
                print("El salario no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Salario inválido. Debe ser un número.")

    nif = input("NIF: ")
    telefono = input("Teléfono: ")

    registros.append([nombre, edad, salario, nif, telefono])

    print(f"Registro agregado. Total de registros: {len(registros)}")
    return registros

def eliminar_registro(registros):
    if not registros:
        print("No hay registros para eliminar.")
        return registros

    imprimir_registros(registros) # Mostrar registros para que el usuario elija
    print(f"\nEliminar registro (1-{len(registros)}):")

    while True:
        try:
            posicion_str = input(f"Ingrese la posición del registro a eliminar (o 0 para cancelar): ")
            if not posicion_str:
                print("La posición no puede estar vacía.")
                continue
            posicion = int(posicion_str)

            if posicion == 0:
                print("Eliminación cancelada.")
                return registros

            if posicion < 1 or posicion > len(registros):
                print(f"La posición debe estar entre 1 y {len(registros)}.")
            else:
                # Eliminar el registro (convertir a índice de 0)
                del registros[posicion - 1]
                print(f"Registro en posición {posicion} eliminado. Total de registros: {len(registros)}")
                break
        except ValueError:
            print("Debe ingresar un número válido para la posición.")
    return registros

def guardar_registros(nombre_fichero, registros):
    """Guarda todos los registros de la matriz en el archivo CSV."""
    try:
        with open(nombre_fichero, 'w', encoding='utf-8') as archivo:
            for registro in registros:
                # Convertir salario a cadena con coma como separador decimal
                # y asegurar que los otros campos sean cadenas también
                campos_str = [
                    str(registro[0]),
                    str(registro[1]),
                    str(registro[2]).replace('.', ','), # Salario con coma
                    str(registro[3]),
                    str(registro[4])
                ]
                linea = ';'.join(campos_str) + '\n'
                archivo.write(linea)
        print(f"Se han guardado {len(registros)} registros en '{nombre_fichero}'")
    except Exception as e:
        print(f"Error al guardar el archivo '{nombre_fichero}': {e}")

def mostrar_menu():
    print("\n" + "="*40)
    print("GESTOR DE REGISTROS MEJORADO")
    print("="*40)
    print("1. Leer registros del archivo CSV")
    print("2. Mostrar todos los registros")
    print("3. Agregar un nuevo registro")
    print("4. Eliminar un registro")
    print("5. Guardar registros en archivo")
    print("6. Salir")
    print("="*40)


# --- Programa Principal ---
if __name__ == "__main__":
    lista_registros = []
    nombre_fichero_csv = 'registros.csv' # Nombre por defecto del archivo

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            lista_registros = leer_registros(nombre_fichero_csv)
        elif opcion == '2':
            imprimir_registros(lista_registros)
        elif opcion == '3':
            lista_registros = agregar_registro(lista_registros)
        elif opcion == '4':
            lista_registros = eliminar_registro(lista_registros)
        elif opcion == '5':
            guardar_registros(nombre_fichero_csv, lista_registros)
        elif opcion == '6':
            print("Gracias por usar el Gestor de Registros Mejorado!")
            break
        else:
            print("Opción no válida. Seleccione una opción del 1 al 6.") 