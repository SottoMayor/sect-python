from random import randint

fake_id = randint(0, 99999)


class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque=0, id=fake_id):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

        self.quantidade_escolhida = 0
        self.em_estoque = self.quantidade_em_estoque > 0

    def tirar_de_estoque(self):
        self.em_estoque = False
        self.quantidade_em_estoque = 0

    def por_em_estoque(self, quantidade=1):
        self.em_estoque = True
        self.quantidade_em_estoque = quantidade

    def retirar_quantidade_em_estoque(self):
        self.quantidade_em_estoque = self.quantidade_em_estoque - \
            1 if self.quantidade_em_estoque > 0 else 0
        return self.quantidade_em_estoque

    def adicionar_quantidade_escolhida(self):
        self.quantidade_escolhida += 1
        return self.quantidade_escolhida

    def __str__(self):
        return f'{self.nome}-({self.id}) custa R$ {self.preco} com ' + \
            f'{self.quantidade_escolhida} unidade(s) em seu carrinho. ' + \
            (
                f'Produto em estoque com {self.quantidade_em_estoque} unidades'
                if self.em_estoque else 'Produto em falta!'
            )


class Boleria(Produto):
    def __init__(
        self, nome, preco, id=fake_id, sabor='', cobertura='', recheio=''
    ):
        super().__init__(nome, preco, id=id)
        self.sabor = sabor
        self.cobertura = cobertura
        self.recheio = recheio

    def mudar_cobertura(self, nova_cobertura):
        self.cobertura = nova_cobertura

    def mudar_recheio(self, novo_recheio):
        self.recheio = novo_recheio

    def __str__(self):
        return f'{self.nome} (ID {self.id})-> Bolo sabor de {self.sabor}, ' + \
            (f'cobertura de {self.cobertura}, ' if self.cobertura
             else 'sem cobertura, ') + \
            (f'recheio de {self.recheio}.' if self.recheio else 'sem recheio.')


class CaixaRegistradora:
    def __init__(self, nome_estabelecimento):
        self.nome_estabelecimento = nome_estabelecimento
        self.carrinho = []

    def __iter__(self):
        return self.carrinho.__iter__()

    def procurar_produto_por_id(self, id):
        produto_no_carrinho = [
            produto for produto in self.carrinho if produto.id == id
        ]

        if(produto_no_carrinho):
            return '[Consulta feita pelo carrinho] -> ' + \
                str(produto_no_carrinho[0])
        else:
            return 'Esse produto não existe no carrinho!'

    def ver_carrinho(self):
        print('[Atenção]: Revise seu pedido...')
        for produto in self.carrinho:
            print(produto)

    def _atualizar_produto_no_carrinho(self, produto, quantidade=1):
        if(isinstance(produto, Produto)):
            for _ in range(quantidade):
                if(produto.quantidade_em_estoque
                        >= produto.quantidade_escolhida):
                    produto.retirar_quantidade_em_estoque()
                    produto.adicionar_quantidade_escolhida()

    def adicionar_produto(
        self, produto, quantidade=1
    ):
        if(isinstance(produto, Produto) and quantidade > 0):
            self.carrinho.append(produto)
            self._atualizar_produto_no_carrinho(produto, quantidade)
        else:
            return

    def fechar_conta(self):
        total = 0
        for produto in self.carrinho:
            total += (produto.preco * produto.quantidade_escolhida)
        total_arredondado = round(total, 2)

        self.ver_carrinho()
        print(f'Total R${total_arredondado}')

        return total_arredondado


bolo_de_cenoura = Boleria('Pedido da Dona Ana', 35.45,
                          id=10, sabor='cenoura', cobertura='chocolate')
print(bolo_de_cenoura)
bolo_de_cenoura.mudar_recheio('chocolate belga')
print(bolo_de_cenoura)

bolo_de_milho = Boleria('Pedido do Ricardão', 12.9,
                        id=12, sabor='milho')
print(bolo_de_milho)

bolo_de_casamento = Boleria(
    'Pedido Mãe Joana', 300, id=1000, sabor='formigueiro',
    cobertura='chocolate premium com gotas de ouro', recheio='doce de cupuaçú'
)

print(bolo_de_casamento)
