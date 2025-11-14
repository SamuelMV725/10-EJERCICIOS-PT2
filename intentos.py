usuario_correcto = "admin"
contraseña_correcta = "1234"
intentos = 0

while intentos < 3:
    usuario = input("Ingrese el usuario: ").strip()
    contraseña = input("Ingrese la contraseña: ").strip()
    
    if not usuario and not contraseña:
        print("Intento vacío, no cuenta.")
        continue  # No contar el intento si ambos campos están vacíos
    
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Acceso exitoso.")
        break
    else:
        intentos += 1
        if usuario != usuario_correcto:
            print("Usuario incorrecto.")
        if contraseña != contraseña_correcta:
            print("Contraseña incorrecta.")
        
        if intentos == 3:
            print("Número máximo de intentos alcanzado.")
