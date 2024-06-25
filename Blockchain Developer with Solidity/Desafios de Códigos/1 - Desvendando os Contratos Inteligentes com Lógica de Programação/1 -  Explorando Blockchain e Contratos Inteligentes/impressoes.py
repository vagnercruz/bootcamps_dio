# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Dicionário que mapeia cada termo à sua respectiva descrição
descricoes = {
    "NFT": "Token digital na blockchain que representa um ativo único",
    "Mineração": "Processo de validar e registrar transações na blockchain",
    "Cadeia de Blocos": "Sequência de blocos com informações registradas na blockchain",
    "Ethereum": "Plataforma que executa contratos inteligentes e DApps"
}

# Função responsável por receber um termo e retornar sua respectiva descrição
def descrever_termo(termo):
    return descricoes.get(termo, "Termo desconhecido")

# Imprime a descrição do termo fornecido
print(descrever_termo(entrada))