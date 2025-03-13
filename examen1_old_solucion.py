# Programa de menú con opciones para potencia y cuadrado
while True:
    print("\nMENU:")
    print("1. (P)otencia")
    print("2. (C)uadrado")
    print("3. (S)alir")
    
    opcion = input("Seleccione una opción (1, 2, 3, P, C, S): ").upper()
    
    # Opción 1 - Potencia sin usar operador **
    
    if opcion == "1" or opcion == "P":
        
        # Solicitar los dos números
        
        while True:
            try:
                base = float(input("Introduzca el primer número: "))
                break
            except ValueError:
                print("Error: Debe introducir un número decimal válido.")
        
        while True:
            try:
                exponente = int(input("Introduzca el segundo número (potencia): "))
                break
            except ValueError:
                print("Error: Debe introducir un número entero válido.")
        
        # Calcular potencia sin usar **
        
        resultado = 1
        if exponente >= 0:
            for _ in range(exponente):
                resultado *= base
        else:
            for _ in range(-exponente):
                resultado *= 1/base
        
        print(f"{base} elevado a {exponente} = {resultado}")
    
    # Opción 2 - Comprobar cuadrados en listas
    
    elif opcion == "2" or opcion == "C":
        
        # Listas predefinidas
        lista1 = [2, -3, 5, 0, 7, -1]
        lista2 = [4, 9, 25, 0, 49, 1]
        
        # Comprobar cuáles cumplen
        elementos_correctos = []
        elementos_incorrectos = []
        
        for i in range(len(lista1)):
            if lista1[i] ** 2 == lista2[i]:
                elementos_correctos.append(i)
            else:
                elementos_incorrectos.append(i)
        
        # Mostrar resultados
        print(f"Lista 1: {lista1}")
        print(f"Lista 2: {lista2}")
        
        if not elementos_incorrectos:
            print("Todos los elementos están correctos.")
            print(f"Posiciones correctas: {elementos_correctos}")
        else:
            print(f"Hay {len(elementos_correctos)} elementos correctos en las posiciones: {elementos_correctos}")
            print(f"Hay {len(elementos_incorrectos)} elementos incorrectos en las posiciones: {elementos_incorrectos}")
            
            # Preguntar si quiere corregir
            corregir = input("¿Desea corregir los elementos incorrectos? (S/N): ").upper()
            if corregir == "S":
                for pos in elementos_incorrectos:
                    lista2[pos] = lista1[pos] ** 2
                print("Listas corregidas:")
                print(f"Lista 1: {lista1}")
                print(f"Lista 2: {lista2}")
        
        # Encontrar el elemento mayor de la lista 1 y su posición
        mayor = lista1[0]
        pos_mayor = 0
        
        for i in range(1, len(lista1)):
            if lista1[i] > mayor:
                mayor = lista1[i]
                pos_mayor = i
        
        print(f"El elemento mayor de la lista 1 es {mayor} y está en la posición {pos_mayor}")
    
    # Opción 3 - Salir
    elif opcion == "3" or opcion == "S":
        print("Programa finalizado.")
        break
    
    # Opción no válida
    else:
        print("Error: Opción no válida.")
