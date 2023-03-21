# condiciones

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M o F): ")

if (sexo == "F" and nombre[0].lower() < "m") or (sexo == "M" and nombre[0].lower() > "n"):
    print("Usted pertenece al grupo A.")
else:
    print("Usted pertenece al grupo B.")