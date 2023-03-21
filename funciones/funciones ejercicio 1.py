def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    
    cantidad_con_iva = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return cantidad_con_iva

total = calcular_total_factura(100, 10)
print(total)

total = calcular_total_factura(100)
print(total)
