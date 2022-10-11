# Operador ** agrupa params nomeados, em forma de DICIONÁRIO, dentro da
# variável kwargs.

# Função que mostra informações de nome
from time import sleep


def mostra_nome(nome='David'):
    print(f'Nome: {nome}')


# Função que mostra informações de nome e idade
def mostra_nome_idade(nome='David', idade=21):
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')


# Como fazer para mostrar informações de forma mais flexivel,
# sem depender(diretamente) de parâmetros nomeados da função??????!
# Para isso usamos o **kwargs

def mostra_informacoes(**kwargs):
    dicionario_com_informacoes = kwargs

    print('Confira as informações a seguir...')
    for chave, valor in dicionario_com_informacoes.items():
        print(f'{chave} -> {valor}')


pessoa = {
    'nome': 'David', 'idade': 21, 'jogador_caro': True,
    'linguagens_programacao': ['python', 'javascript', 'ruby', 'haskell']
}

mostra_informacoes(**pessoa)


print('\n' + 30*'#-' + '\n')  # Demarcador


# timer
def timer(contagem=30, pausa_entre_segundos=1, ativo=True, buzina_ligada=True):
    if(not ativo):
        return 'O alarme não está ativo!'

    for _ in range(0, contagem):
        sleep(pausa_entre_segundos)

    return 'TRIIIIIIM!' if buzina_ligada else '*Buzina Desligada*'


# print(timer()) # Desse modo timer está usando os valores padrões.
print(timer(ativo=False))
print(timer(buzina_ligada=False, pausa_entre_segundos=2, contagem=3))


def timer_flexivel(**kwargs):
    # Antes de todo é preciso extrair os parâmetros passados em kwargs
    nome_pessoa = kwargs.get('nome', 'Anônimo')
    ativo = kwargs.get('ativo', True)
    contagem = kwargs.get('contagem', 30)
    pausa_entre_segundos = kwargs.get('pausa_entre_segundos', 1)
    buzina_ligada = kwargs.get('buzina_ligada', True)

    if(not ativo):
        return 'O alarme não está ativo!'

    print(f'Bom dia {nome_pessoa}. Espero que tenha dormido como um bebê!')

    for _ in range(0, contagem):
        sleep(pausa_entre_segundos)

    return 'TRIIIIIIM!' if buzina_ligada else '*Buzina Desligada*'


timer_config = {
    'contagem': 5, 'pausa_entre_segundos': 1,
    'ativo': True, 'buzina_ligada': True
}
print(timer_flexivel(**timer_config))
print(timer_flexivel(nome='David', buzina_ligada=False))
