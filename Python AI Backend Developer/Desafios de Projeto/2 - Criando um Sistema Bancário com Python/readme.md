# Sistema de Banco em Python

Este é um simples sistema de banco em Python que permite aos usuários realizar operações básicas como depositar dinheiro, sacar dinheiro e visualizar o extrato da conta.

## Funcionalidades

- **Depositar**: Permite ao usuário depositar uma quantia em dinheiro na conta.
- **Sacar**: Permite ao usuário sacar uma quantia em dinheiro da conta, respeitando o limite diário de saques e o limite de valor por saque.
- **Extrato**: Permite ao usuário visualizar o extrato da conta, mostrando todas as operações realizadas e o saldo atual.
- **Sair**: Permite ao usuário sair do sistema.

## Requisitos

- Python 3.12.3 ou superior

## Estrutura do Código

O código está organizado em funções para cada operação (depositar, sacar, extrato) e um loop principal para controlar o menu e as interações com o usuário. Aqui está uma visão geral das funções:

- `mostrar_menu()`: Exibe o menu e captura a opção do usuário.
- `depositar(saldo, extrato)`: Realiza a operação de depósito e atualiza o saldo e o extrato.
- `sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)`: Realiza a operação de saque, verificando os limites e atualizando o saldo, o extrato e o número de saques.
- `mostrar_extrato(saldo, extrato)`: Exibe o extrato da conta.
- `main()`: Função principal que inicializa as variáveis e controla o loop do menu.