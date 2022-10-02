pessoa = {'nome': 'David Sotto Mayor', 'carros': [
    'ferrari', 'celta', 'corsa'], 'maior_idade': True, 'dinheiro_conta': 55.75,
    'cidade_estado': ('Manaus', 'AM')}

# Escrever o nome da pessoa de trás pra frente
print(pessoa['nome'][::-1])

# Mostrar a lista de carros e a quantidade, excluir e adicionar um carro
print(pessoa['carros'], len(pessoa['carros']))
pessoa['carros'].pop()
pessoa['carros'].append('civic')
print(pessoa['carros'], len(pessoa['carros']))

# Alterar dinheiro_conta
pessoa['dinheiro_conta'] = 4500

# Adicionar campo 'jogador' como booleano
pessoa['jogador'] = True

# Verificar se a cidade da pessoa é Manaus (Dica: use o operador 'in')
manauara = 'Manaus' in pessoa['cidade_estado']
print('MANAUARA da gema!' if manauara else 'Não é manauara')

# excluir o campo carros
del pessoa['carros']

# Montar uma frase usando os dados do dicionario (Dica: use a interpolação)
mensagem = f'Olá! Eu sou {pessoa["nome"]} e tenho R${pessoa["dinheiro_conta"]} na conta!'
print(mensagem)

# Exclua todos os campos do dicionario de uma vez
pessoa.clear()
print(pessoa)
