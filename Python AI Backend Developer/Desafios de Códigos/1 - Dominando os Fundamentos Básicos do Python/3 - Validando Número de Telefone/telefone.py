import re

def validate_numero_telefone(phone_number):
    # Define um padrão regex para validar números de telefone no formato (XX) 9XXXX-XXXX
    pattern = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    
    # Verifica se o número de telefone fornecido corresponde ao padrão definido
    return "Número de telefone válido." if re.match(pattern, phone_number) else "Número de telefone inválido."

# Solicita ao teste da plataforma que insira um número de telefone
phone_number = input()

# Chama a função e imprime o resultado
print(validate_numero_telefone(phone_number))
