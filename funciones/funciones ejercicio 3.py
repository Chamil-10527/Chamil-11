# Funciones 

def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    palabra_max = ''
    frec_max = 0
    for palabra, frec in frecuencias.items():
        if frec > frec_max:
            palabra_max = palabra
            frec_max = frec
    return (palabra_max, frec_max)

cadena = "Hola mundo, hola Python, hola programación"
frecuencias = contar_palabras(cadena)
print(frecuencias)
palabra_max, frec_max = palabra_mas_repetida(frecuencias)
print(f"La palabra más repetida es '{palabra_max}' con frecuencia {frec_max}")