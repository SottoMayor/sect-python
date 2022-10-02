# Obtendo dados a partir do teclado - coletados em formato str por padrão.
nome = input('Escreva seu nome: ')
# nome = str(input('Escreva seu nome: ' ))
idade = int(input('Escreva sua idade: '))
dinheiro = float(input('Escreva quantos R$ você tem na carteira: '))

# Concatenação
concatenacao_padrao = 'Oi! Eu sou ' + nome + ' tenho ' + \
    str(idade) + ' anos e tenho R$' + str(dinheiro) + ' na carteira!'
print(concatenacao_padrao)

concatenacao_f_string = f'Oi! Eu sou {nome} tenho {idade} anos e tenho R${dinheiro} na carteira!'
print(concatenacao_f_string)
