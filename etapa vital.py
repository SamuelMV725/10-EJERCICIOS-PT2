edad = int(input("Ingrese su edad: "))
nivel = input("¿Estudia o trabaja? (estudia/trabaja/ninguno): ").strip().lower()

if edad < 0 or edad > 120:
    print("Edad no válida.")
elif edad < 6:
    print("Etapa: Infante")
elif 6 <= edad <= 17 and nivel == "estudia":
    print("Etapa: Estudiante escolar")
elif 18 <= edad <= 25 and nivel == "estudia":
    print("Etapa: Universitario")
elif edad > 25 and nivel == "trabaja":
    print("Etapa: Adulto activo")
elif edad > 60 and nivel != "trabaja":
    print("Etapa: Adulto mayor jubilado")
else:
    print("Etapa: No determinada")
