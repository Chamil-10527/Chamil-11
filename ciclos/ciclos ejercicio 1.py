# Ciclos

cantidad = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual: "))
num_anios = int(input("Ingrese el número de años: "))

for i in range(1, num_anios+1):
    capital = cantidad * ((1 + (interes_anual/100)) ** i)
    print("Capital obtenido en el año", i, ":", round(capital, 2))