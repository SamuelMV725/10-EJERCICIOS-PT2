edad = int(input("Edad: "))
licencia = input("¿Tiene licencia vigente? (si/no): ").lower()
vehiculo = input("¿Posee usted vehiculo propio o prestamo autorizado? (propio/prestado/ninguno) ").lower()


if edad >= 18 and licencia == "si" and (vehiculo == "propio" or vehiculo == "prestamo"): print ("Participante Apto")
else:
    print ("Participante No Apto")