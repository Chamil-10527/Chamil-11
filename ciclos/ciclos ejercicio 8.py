creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

# Mostrar los créditos de cada asignatura
for asignatura, creditos_asig in creditos.items():
    print(f"{asignatura} tiene {creditos_asig} créditos")

# Calcular y mostrar el número total de créditos
total_creditos = sum(creditos.values())
print(f"El total de créditos del curso es {total_creditos}")