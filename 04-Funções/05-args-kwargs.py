# Também é possível usar *args e **kwargs juntos, dessa forma estamos
# capturando todos os parâmetros de forma genérica.

# Atenção! Na declaração da função *args deve vir primeiro que **kwargs


def todos_os_params(*args, **kwargs):
    print(f'*args: {args}')
    print(f'*kwargs: {kwargs}')


todos_os_params(1, 2, 'David', [{'produto': 'caneta', 'preco': 1.99}],
                carro='Ferrari', sistema_operacional='Linux', idade=21)


print('\n' + 30*'#-' + '\n')  # Demarcador

# args -> Todos as notas do aluno
# kwargs -> informações sobre o aluno


def notas(*args, **kwargs):
    tupla_de_notas = args
    dicionario_info_aluno = kwargs

    soma_das_notas = 0
    for nota in tupla_de_notas:
        soma_das_notas += nota
    media = round(soma_das_notas / len(tupla_de_notas), 2)

    for chave, valor in dicionario_info_aluno.items():
        print(f'{chave}: {valor}')

    mensagem = 'APROVADO!' if media >= 7 else 'reporvado :('
    print(mensagem)

    return media


print(notas(10, 10, 7, nome='David', serie='3° ano E.M.'))
