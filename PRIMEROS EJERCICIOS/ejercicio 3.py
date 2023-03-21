def contar_letras(nombre):
    nombre_mayus = nombre.upper() # Convertir a mayúsculas
    n_letras = len(nombre) # Obtener número de letras
    print(f"{nombre_mayus} tiene {n_letras} letras")
    
contar_letras("Juan")