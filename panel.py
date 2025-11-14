def mostrar_menu():
    print("\nMenú de control doméstico:")
    print("1. Encender luces")
    print("2. Activar calefacción")
    print("3. Ver estado")
    print("4. Salir")

estado_luces = False
estado_calefaccion = False
es_de_noche = True  # Simulación de si es de noche
temperatura = 17  # Temperatura en grados Celsius

while True:
    mostrar_menu()
    opcion = input("Elija una opción: ")
    
    if opcion == '1':
        if es_de_noche:
            estado_luces = True
            print("Luces encendidas.")
        else:
            print("No se pueden encender las luces durante el día.")
    
    elif opcion == '2':
        if estado_luces and temperatura < 18:
            estado_calefaccion = True
            print("Calefacción activada.")
        else:
            if not estado_luces:
                print("No se puede activar la calefacción sin luces encendidas.")
            if temperatura >= 18:
                print("La calefacción no es necesaria, la temperatura es suficiente.")
    
    elif opcion == '3':
        print(f"Estado de luces: {'Encendidas' if estado_luces else 'Apagadas'}")
        print(f"Estado de calefacción: {'Activada' if estado_calefaccion else 'Desactivada'}")
    
    elif opcion == '4':
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción no válida.")
