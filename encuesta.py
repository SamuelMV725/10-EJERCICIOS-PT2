afirmativas = 0
negativas = 0

while True:
    edad = int(input("Ingrese su edad (0 para terminar): "))
    if edad <= 0:
        break
    
    respuesta = input("¿Te gusta programar? (si/no): ").strip().lower()
    
    if respuesta == "si":
        afirmativas += 1
    elif respuesta == "no":
        negativas += 1
    else:
        print("Respuesta inválida. Por favor ingrese 'si' o 'no'.")

print(f"Respuestas afirmativas: {afirmativas}")
print(f"Respuestas negativas: {negativas}")
