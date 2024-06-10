# Criando uma Lista 'itens' para armazenar os equipamentos
itens = []

# Loop para solicitar os itens ao usuário
for i in range(3):
    item = input()
    
    # Adicionando o item à lista "itens"
    itens.append(item)

# Exibindo a lista de itens
print("Lista de Equipamentos:")
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
