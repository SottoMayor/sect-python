pessoa = {'nome': 'David Sotto Mayor', 'carros': [
    'ferrari', 'celta', 'corsa'], 'maior_idade': True, 'dinheiro_conta': 55.75,
    'cidade_estado': ('Manaus', 'AM')}

# Verificar se a pessoa é maior de idade e tem mais de R$ 100 na conta (*)
maior_idade_mais_de_100_reais = pessoa['maior_idade'] and pessoa['dinheiro_conta'] > 100
print(maior_idade_mais_de_100_reais)

# Verificar se a pessoa tem pelo menos 1 carro (**)
ao_menos_1_carro = len(pessoa['carros']) >= 1
print(ao_menos_1_carro)

# Se (*) e (**) forem verdadeiros, então a pessoa está apta a ir tomar uma
# gelada.
# Escreva uma mensagem se positiva se a pessoa estiver apta a sair, caso
# contrário escreva uma mensagem negativa.
mensagem = 'Pode ir tomar a gelada!' if maior_idade_mais_de_100_reais and ao_menos_1_carro else 'É melhor ficar em casa mesmo!'
