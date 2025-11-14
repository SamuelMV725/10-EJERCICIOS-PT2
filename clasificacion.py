# Solicitar valor de la compra y tipo de membresía
try:
    monto = float(input("Ingrese el valor total de la compra: "))
    if monto < 0:
        raise ValueError("Monto inválido")
except ValueError:
    print("Error: Monto inválido.")
    exit()

membresia = input("Ingrese tipo de membresía (activa/temporal/ninguna): ").strip().lower()

if monto >= 1000 and membresia == "activa":
    print("Cliente Premium.")
elif monto >= 500 or membresia == "temporal":
    print("Cliente Frecuente.")
else:
    print("Cliente Regular.")
