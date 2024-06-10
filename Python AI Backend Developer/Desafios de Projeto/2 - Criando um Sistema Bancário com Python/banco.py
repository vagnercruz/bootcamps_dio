def mostrar_menu():
    menu = """
    ==============================   MENU  =============================
                            [d] - Depositar
                            [s] - Sacar
                            [e] - Extrato
                            [q] - Sair
    ===================================================================
    """
    return input(menu)

def depositar(saldo, extrato):
    valor = input("Informe o valor a ser depositado: ")
    try:
        valor = float(valor)
        if valor > 0:
            saldo += valor
            extrato += f"Depósito realizado: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso! R$ {valor:.2f}\n")
        else:
            print("Operação falhou: O valor informado é inválido")
    except ValueError:
        print("Operação falhou: Por favor, insira um número válido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    valor = input("Informe o valor de saque: ")
    try:
        valor = float(valor)
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! O número máximo de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque realizado: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso! R$ {valor:.2f}\n")
        else:
            print("Operação falhou: O valor informado é inválido.")
    except ValueError:
        print("Operação falhou: Por favor, insira um número válido.")
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("============================== EXTRATO ==============================")
    print("Não foram realizadas movimentações na conta." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=====================================================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = mostrar_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)
        elif opcao == "e":
            mostrar_extrato(saldo, extrato)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione um comando válido.")

if __name__ == "__main__":
    main()
