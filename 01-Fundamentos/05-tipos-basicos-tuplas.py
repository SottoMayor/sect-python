# Definimos tupla com ()
alunos = ('Ana', 'Bia', 'Carlos', 'David', 'Elias', 'Fernanda')

print('Qtt de alunos', len(alunos))

print('\n' + 30*'#-' + '\n')  # Demarcador

# A tupla é uma estrutura indexada
print(alunos[0])
print(alunos[-1])
# print(alunos[50]) # Erro!
print(alunos.index('David'), alunos[3])

# Fatiamento de listas
alguns_alunos = alunos[1:4]
print(alguns_alunos)
print(alunos[1:-4])
print(alunos[::2])
# Não é possível sobrescrever elementos pelo indice, já que a tupla é imutável!
# alunos[1] = 'David'  # Erro!

# OBS: ('Bia') é diferente de ('Bia', )
print(type(('Bia')))  # string
print(type(('Bia', )))  # tupla com um único elemeto
