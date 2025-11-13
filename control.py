restringidos = ["admin", "root", "banned"]
usuario = input ("nombre de usuario: ").lower()
codigo = input ("codigo numerico: ")


if usuario in restringidos:
    print("acceso denegado= ususario restringido. ")
elif not codigo.isdigit():
    print("codigo invalido, debe ser numerico. ")
else:
    codigo = int(codigo)
    if codigo % 2 == 0 or str(codigo).endswith("7"):
        print("acceso permitido")
    else:
        print("acceso denegado: codigo no cumple con las condiciones. ")    