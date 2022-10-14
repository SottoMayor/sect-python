
'''
    Classe Produto.
    Atributos (características) -> id(int), nome(string), preco(float),
                quantidade_em_estoque(int), quantidade_escolhida(int),
                em_estoque(boolean)

    Métodos (comportamentos) -> contrustor, tirar_de_estoque, por_em_estoque,
                retirar_quantidade_em_estoque, adicionar_quantidade_escolhida

    Passos:
        1 - Definindo métodos
        2 - Definindo atributos
        3 - Construindo métodos retirar_quantidade_em_estoque e
            adicionar_quantidade_escolhida
        4 - Construindo métodos tirar_de_estoque e por_em_estoque,
            instânciando um produto
        5 - Método mágico __str__ e identificação do bug
        6 - Arrumando o bug no método retirar_quantidade_em_estoque
        --- FIM ---
'''

from random import randint

fake_id = randint(0, 99999)

# OBS: self é uma palavra reservada no Python, com ela conseguimos acessar os
# atributos e métodos de uma classe.


class Produto:
    # Construtor
    def __init__(self, nome, preco, quantidade_em_estoque=0, id=fake_id):
        # Aqui vão os atributos (de instância)
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

        self.quantidade_escolhida = 0
        self.em_estoque = self.quantidade_em_estoque > 0

    # Att em_estoque para False e zerar quantidade_em_estoque
    def tirar_de_estoque(self):
        self.em_estoque = False
        self.quantidade_em_estoque = 0

    # Att em_estoque para True e passar um valor para quantidade_em_estoque
    def por_em_estoque(self, quantidade=1):
        # Caso o parâmetro quantidade não seja preenchido, temos por padrão 1

        self.em_estoque = True
        self.quantidade_em_estoque = quantidade

    # Retirar uma quantidade do atributo quantidade_em_estoque
    def retirar_quantidade_em_estoque(self):
        if(self.quantidade_em_estoque > 0):
            nova_quantidade = self.quantidade_em_estoque - 1
        else:
            nova_quantidade = 0

        self.quantidade_em_estoque = nova_quantidade
        return self.quantidade_em_estoque

    # Adicionar uma quantidade em quantidade escolhida
    def adicionar_quantidade_escolhida(self):
        self.quantidade_escolhida += 1
        return self.quantidade_escolhida

    # Método Mágico __str__
    def __str__(self):
        return f'{self.nome}-({self.id}) custa R$ {self.preco} com ' + \
            f'{self.quantidade_escolhida} unidade(s) em seu carrinho. ' + \
            f'Produto em estoque com {self.quantidade_em_estoque} unidades'


calculadora = Produto('Calculadora Científica', 13.45, 1300, 10)
print(calculadora)

caderno = Produto('Cardeno do Max Steel', 25, 1)
print(caderno)
caderno.retirar_quantidade_em_estoque()
caderno.retirar_quantidade_em_estoque()
print(caderno)