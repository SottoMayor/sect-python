nome = 'David Sotto Mayor'
# Para definir usamos []
nomes = nome.split(' ')  # [ 'David', 'Sotto', 'Mayor' ]
print(nomes)

print('\n' + 30*'#-' + '\n')  # Demarcador

# Inserir e retirar elementos na lista
nomes.append('Maciel')
nomes.append('Fernandes')
print(nomes)
print('tamanho da lista:', len(nomes))

nomes.remove('Maciel')
print(nomes)
print('tamanho da lista:', len(nomes))

nomes.pop()
print(nomes)
print('tamanho da lista:', len(nomes))

print('\n' + 30*'#-' + '\n')  # Demarcador

# Uma lista pode agrupar vários elementos diferentes
mistureba = ['david', 21, 0.5, {'estudante': True}]
mistureba.remove({'estudante': True})
print(mistureba)
# inverter elementos da lista
mistureba.reverse()
print(mistureba)

print('\n' + 30*'#-' + '\n')  # Demarcador

# Uma lista pode agrupar outras listas
lista_de_listas = []
lista_de_listas.append([1, 2, 3])
lista_de_listas.append([4, 5, 6])
print(lista_de_listas)
print(lista_de_listas[0][0])
print('\n' + 30*'#-' + '\n')  # Demarcador

# Como as strings, a lista também é uma estrutura indexada!
alunos = ['Ana', 'Bia', 'Carlos', 'David', 'Elias', 'Fernanda']
print(alunos[0])
print(alunos[-1])
# print(alunos[50]) # Erro!
print(alunos.index('David'), alunos[3])

# Fatiamento de listas
alguns_alunos = alunos[1:4]
print(alguns_alunos)
print(alunos[1:-4])
print(alunos[::2])
# deletando elementos por index
del alunos[3]
print(alunos)
del alunos[2:]
print(alunos)
# Sobrescrevendo elementos pelo indice, já que a lista é mutável!
alunos[1] = 'David'
print(alunos)
