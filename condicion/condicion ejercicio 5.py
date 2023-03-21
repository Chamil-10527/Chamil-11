# condiciones

puntuacion = float(input("Ingrese su puntuación: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
    dinero = 0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = 2400 * puntuacion
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero = 2400 * puntuacion

print("Su nivel de rendimiento es:", nivel)
print("Recibirá", dinero, "euros.")