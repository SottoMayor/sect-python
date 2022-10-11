# Escreva uma função que receba qualquer string de argumentos e 1 parâmetro
# booleanos nomeados 'retorna_lista', esse último por padrão deve ser True.

# Objetivo: A função deve retornar uma lista de strings sem repetições, e só
# deve retornar apenas se retorna_lista for True. Caso retorna_lista seja False
# retornar a mensagem 'O retorno da lista está desabilitado!'.

# Exemplo: Caso retorna_lista seja True e a lista de entrada seja
#  ['David', 'David', 'David', 'Sotto', 'Mayor', 'Sotto', 'Matemática'], então
# o retorno deve ser ['David', 'Sotto', 'Mayor', 'Matem�tica']. Caso
# retorna_lista seja True retornar a mensagem abaixo:
# 'O retorno da lista está desabilitado!'

def unicos(*args, **kwargs):
    # Escreva o código aqui dentro...
    print(f'*args: {args}')
    print(f'**kwargs: {kwargs}')


print(
    unicos('David', 'David', 'David', 'Sotto', 'Mayor', 'Sotto', 'Matemática')
)
