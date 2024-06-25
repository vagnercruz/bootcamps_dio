# Crie uma classe UsuarioTelefone
class UsuarioTelefone:
    # Defina um método especial `__init__`, que é o construtor da classe.
    def __init__(self, nome, numero, plano):
        # Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
        self._nome = nome
        self._numero = numero
        self._plano = plano

    # Método para retornar o nome do usuário
    @property
    def nome(self):
        return self._nome

    # Método para retornar o número do usuário
    @property
    def numero(self):
        return self._numero

    # Método para retornar o plano do usuário
    @property
    def plano(self):
        return self._plano

    # Método especial `__str__` que retorna uma representação em string do objeto
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."

# Entrada da plataforma
nome = input()  
numero = input()  
plano = input()  

# Crie um novo objeto `UsuarioTelefone` com os dados fornecidos
usuario = UsuarioTelefone(nome, numero, plano)

# Imprime a representação em string do objeto, que indica que o usuário foi criado com sucesso
print(usuario)
