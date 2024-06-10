# Classe Plano
class Plano:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    # Método para verificar o saldo atual
    def verificar_saldo(self):
        return self._saldo

    # Método para calcular o custo de uma chamada
    def custo_chamada(self, duracao):
        return 0.10 * duracao

    # Método para deduzir o valor do saldo do plano
    def deduzir_saldo(self, valor):
        self._saldo -= valor

# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano

# Classe UsuarioPrePago que herda de UsuarioTelefone
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

    # Método para permitir que um usuário faça uma chamada telefônica
    def fazer_chamada(self, destinatario, duracao):
        custo = self._plano.custo_chamada(duracao)
        saldo_atual = self._plano.verificar_saldo()

        if saldo_atual >= custo:
            self._plano.deduzir_saldo(custo)
            saldo_restante = self._plano.verificar_saldo()
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

# Recebendo as informações do usuário
nome = input()
numero = input()
saldo_inicial = float(input())

# Criação do objeto UsuarioPrePago com os dados fornecidos
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e mostra o resultado
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
