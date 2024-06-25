# Classe PlanoTelefone
class PlanoTelefone:
    def __init__(self, nome, saldo):
        # Encapsulamento dos atributos
        self._nome = nome
        self._saldo = saldo
    
    # Verificar o saldo do plano
    def verificar_saldo(self):
        if self._saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self._saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

# Classe UsuarioTelefone
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self._nome = nome
        self._plano = plano

    # Verificar o saldo do usuário e gerar uma mensagem personalizada
    def verificar_saldo(self):
        mensagem = self._plano.verificar_saldo()
        return self._plano._saldo, mensagem

# Recebendo as entradas do usuário (nome, plano, saldo)
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)
