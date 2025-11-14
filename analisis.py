# Solicitar tres números enteros
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

# Verificar las condiciones
if n1 > 0 and n2 > 0 and n3 > 0:
    print("Los tres números son positivos.")
elif n1 < 0 or n2 < 0 or n3 < 0:
    print("Al menos uno de los números es negativo.")
elif (n1 == 0) + (n2 == 0) + (n3 == 0) == 1:
    print("Exactamente uno de los números es cero.")
