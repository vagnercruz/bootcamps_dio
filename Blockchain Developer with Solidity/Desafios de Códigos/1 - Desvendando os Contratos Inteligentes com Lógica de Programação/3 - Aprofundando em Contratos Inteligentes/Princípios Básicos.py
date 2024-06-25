# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um termo e retornar sua respectiva descrição
def descrever_termo(termo):
    if termo == "DAOs":
        return "Organizações autônomas descentralizadas"
    elif termo == "DApps":
        return "Aplicações descentralizadas que operam em uma rede blockchain"
    elif termo == "Solidity":
        return "Linguagem de programação utilizada nos contratos inteligentes"
    elif termo == "Oráculos":
        return "Entidades que fornecem dados externos aos contratos inteligentes"
    elif termo == "Gas Fees":
        return "Taxas pagas para realizar transações e executar contratos"
    else:
        return "Termo desconhecido"

# Imprime a descrição do termo fornecido
print(descrever_termo(entrada))
