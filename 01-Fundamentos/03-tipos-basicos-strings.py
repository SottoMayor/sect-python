# Podemos definir strings com aspas simples ('') ou duplas ("")
saudacao = 'Hello World'

# Strings são indexadas
primeira_letra_saudacao = saudacao[0]
ultima_letra_saudacao = saudacao[-1]
print(primeira_letra_saudacao, ultima_letra_saudacao)

print('\n' + 30*'#-' + '\n') # Demarcador

# Strings são imutáveis
# saudacao[0] = 'A' # ERRO!

# Escaping de caracteres
instrucao = 'Aperte no botão escrito \'AÇÃO\'.'
print(instrucao)
print("Ele disse \"mãos ao alto!\"")
# Podemos usar aspas simples dentro de aspas duplas também, e vice-versa
print('Aperte no botão escrito "AÇÃO".')
print("Ele disse 'mãos ao alto!'")

# String com múltiplas linhas
texto = '''
    Olá!
    Eu sou David.
    Python é uma maravilha!
'''
texto_sem_espacos = """
Olá!
Eu sou David.
Python é uma maravilha!
"""
print(texto)
print(texto_sem_espacos)

print('\n' + 30*'#-' + '\n') # Demarcador

# Manipulação e fatiamento de strings
nome = 'David Sotto Mayor'
# Pegando apenas 1 caracter de uma string
print(nome[0], nome[2], nome[4])
# Pegando uma sequência de caracteres
# string[a:b] -> Pegue uma fatia da string que inicia no número a e termina em b - 1.
print(nome[0:5])
print(nome[5:])
print(nome[6: -1])
print(nome[-5:])
# string[a:b:c] -> Pegue uma fatia da string que inicia no número a e termina em b - 1, de c em c passos.
print(nome, nome[::])
print(nome[::3])
print(nome[::5])
print(nome[::-1])
print(nome[-1:5:-1])

print('\n' + 30*'#-' + '\n') # Demarcador

# Funções interessantes para strings
print(nome.upper())
print(nome.lower())
print('david sotto mayor'.capitalize())
print(nome.split(' '))
print(nome.split('a'))
print(len(nome))
