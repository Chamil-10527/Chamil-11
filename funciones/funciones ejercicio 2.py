def decimal_a_binario(numero):
    
    if numero == 0:
        return '0'

    
    digitos_binarios = []


    while numero > 0:
        
        digito_binario = numero % 2
        digitos_binarios.insert(0, str(digito_binario))

        numero //= 2

    
    numero_binario = ''.join(digitos_binarios)
    return numero_binario


def binario_a_decimal(numero):
    
    digitos_binarios = list(numero)

    
    numero_decimal = 0
    for indice, digito_binario in enumerate(digitos_binarios):
        potencia = len(digitos_binarios) - indice - 1
        numero_decimal += int(digito_binario) * 2 ** potencia

    
    return numero_decimal


numero_binario = decimal_a_binario(42)
print(numero_binario)  

numero_decimal = binario_a_decimal('110110')
print(numero_decimal)  


