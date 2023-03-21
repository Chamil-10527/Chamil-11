def invertir_frase(frase):
    frase_invertida = " ".join(frase.split()[::-1]) 
    print(frase_invertida)
    
invertir_frase("Hola mundo, ¿cómo estás?")