asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = {}

for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de {asignatura}: "))
    notas[asignatura] = nota

for asignatura, nota in notas.items():
    if nota >= 5:
        asignaturas.remove(asignatura)

print("Las asignaturas que debe repetir son:")
for asignatura in asignaturas:
    print(asignatura)