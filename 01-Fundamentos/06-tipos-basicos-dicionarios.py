# Dicionários são definidos com {}, são estruturas chave-valor
pessoa = {'nome': 'David Sotto Mayor', 'idade': 21,
          'universitario': True, 'expertise': ['matemática', 'computação']}
print(pessoa)

print('\n' + 30*'#-' + '\n')  # Demarcador

# Acessando valores do dicionário pela chave
print(pessoa['nome'])
print(pessoa['universitario'])

# Dicionarios são mutáveis!
pessoa['universitario'] = False  # Sobrescrever, pois já existe no dic.
pessoa['carro'] = 'peugeot tunado!'  # Adicionar, pois não existe no dic.
print(pessoa)

# Como listas também são mutáveis, podemos acessar uma lista a partir de
# um dicionário e alterá-la
pessoa['expertise'].pop()
pessoa['expertise'].append('otimização')
print(pessoa)

print('\n' + 30*'#-' + '\n')  # Demarcador

# Métodos úteis para dicionário
print(pessoa.items())  # Retorna uma lista com cada chave e valor
print(pessoa.keys())  # Retorna uma lista com cada chave
print(pessoa.values())  # Retorna uma lista com cada valor
# Excluir um par chave-valor
pessoa.pop('nome')
print(pessoa)
del pessoa['carro']
print(pessoa)
# Excluindo todos os elementos de um dicionário
pessoa.clear()
print(pessoa)
