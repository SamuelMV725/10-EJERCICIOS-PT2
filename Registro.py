nombres = []
while True:
    nombre = input("ingrese un nombre (o 'FIN' para terminar): ").strip()
    if nombre == "FIN":
        break
    elif nombre: # Ignorar entradas vacias
        nombres.append(nombre)

#Mostrar resultados
print(f"Total de nombres ingresados: {len(nombres)}")
repetidos = set([x for x in nombres if nombres.count(x) > 1])
if repetidos:
    print(f"Nombres repetidos: {', '.join(repetidos)}")
else:
    print("No hay nombres repetidos.")