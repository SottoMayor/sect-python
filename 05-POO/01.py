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


calculadora = Produto('Calculadora Casio', 3.45, 1300, 10)
caderno = Produto('Caderno', 7.5, 1, 1)
# print(calculadora)
# calculadora.retirar_quantidade_em_estoque()
# print(calculadora)
# calculadora.adicionar_quantidade()
# print(calculadora)
# calculadora.tirar_de_estoque()
# print(calculadora)
# calculadora.por_em_estoque()
# print(calculadora)
# calculadora.por_em_estoque(1300)
# print(calculadora)

loja_do_joao = CaixaRegistradora('Loja do João')

loja_do_joao.adicionar_produto(calculadora, 3)
loja_do_joao.adicionar_produto(caderno, 10)
for produto in loja_do_joao:
    print(produto)

print(loja_do_joao.procurar_produto_por_id(10))
print(loja_do_joao.procurar_produto_por_id(1))

loja_do_joao.fechar_conta()
