'''
    Classe Produto.
    Atributos (características) -> id(int), nome(string), preco(float),
                quantidade_em_estoque(int), quantidade_escolhida(int),
                em_estoque(boolean)

    Métodos (comportamentos) -> contrustor, tirar_de_estoque, por_em_estoque,
                retirar_quantidade_em_estoque, adicionar_quantidade_escolhida

    Passos:
        1 - Definindo métodos
'''


# OBS: self é uma palavra reservada no Python, com ela conseguimos acessar os
# atributos e métodos de uma classe.
class Produto:
    # Construtor
    def __init__(self):
        # Aqui vão os atributos (de instância)
        pass

    # Att em_estoque para False e zerar quantidade_em_estoque
    def tirar_de_estoque(self):
        pass

    # Att em_estoque para True e passar um valor para quantidade_em_estoque
    def por_em_estoque(self):
        pass

    # Retirar uma quantidade do atributo quantidade_em_estoque
    def retirar_quantidade_em_estoque(self):
        pass

    # Adicionar uma quantidade em quantidade escolhida
    def adicionar_quantidade_escolhida(self):
        pass
