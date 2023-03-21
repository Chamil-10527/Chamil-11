def quitar_prefijo_y_extension(num_telefono):
    num_sin_prefijo = num_telefono[4:14] 
    num_sin_extension = num_sin_prefijo[:-3] 
    print(num_sin_extension)
    
quitar_prefijo_y_extension("+34-913724710-56")