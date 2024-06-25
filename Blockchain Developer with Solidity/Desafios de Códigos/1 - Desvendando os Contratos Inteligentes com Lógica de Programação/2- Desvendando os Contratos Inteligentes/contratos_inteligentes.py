# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um termo e retornar sua respectiva descrição
def descrever_termo(termo):
    if termo == "Automação de Acordos":
        return "Permite a execução de contratos baseado em eventos pré-definidos"
    elif termo == "Imutabilidade":
        return "Não pode ser alterado ou modificado após sua criação"
    elif termo == "Execução Autônoma":
        return "Executa automaticamente as condições do código do contrato"
    elif termo == "Interoperabilidade":
        return "Capacidade de interagir e operar com diferentes blockchains"
    else:
        return "Termo desconhecido"

# Imprime a descrição do termo fornecido
print(descrever_termo(entrada))
