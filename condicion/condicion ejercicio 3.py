# condiciones

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))

if edad >= 16 and ingresos >= 1000:
    print("Usted debe tributar.")
else:
    print("Usted no debe tributar.")