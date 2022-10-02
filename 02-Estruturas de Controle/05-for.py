# O laço for é mais popular e geralmente usamos quando queremos percorrer uma
# quantidade definida de elementos

# Podemos dizer que tudo (ou quase tudo) o que o for faz o while também faz,
# mas com uma sintaxe diferente...

# range(x, y, z) -> Função que retorna uma lista de números de x a y-1
# em z passos
for par in range(0, 10, 2):
    print(par)

soma = 0  # acumuladora!
for numero in range(101):
    soma += numero
print(soma)

print('\n' + 30*'#-' + '\n')  # Demarcador

# Nós não necessariamente precisamos usar a variavel definida no for
# Suponha um laço rodando em loop...
soma = 0
for _ in range(10000):  # intervalo suficientemente grande
    print('Rodando')

    # Adicionando +10 na soma a cada iterada
    soma += 7

    if(soma % 2 == 0):
        continue
    else:
        print('soma', soma)

    if(soma > 100):
        print(f'{soma} é maior que 100. O laço será parado.')
        break
print('fora do laço!')

print('\n' + 30*'#-' + '\n')  # Demarcador

# Varredura - Percorrendo estruturas indexadas
# strings
for letra in 'David Sotto Mayor':
    print(letra, end=' ')

print('\n')

# listas
frutas = ['banana', 'laranja', 'pera', 'cupuaçú']
for fruta in frutas:
    print(fruta, end=' ')

print('\n')

# tuplas
eletrodomesticos = ('fogão', 'air fryer', 'máquina de lavar')
for eletrodomestico in eletrodomesticos:
    print(eletrodomestico, end=' ')

print('\n')

# dicionarios
carro = {'marca': 'Hyundai', 'modelo': 'HB20',
         'autonomia': 12.5, 'vidro_eletrico': True}
# Varrendo dicionário pela chave
for chave in carro.keys():
    print(chave, end=' ')
print('\n')
# Varrendo dicionário pelo valor
for valor in carro.values():
    print(valor, end=' ')
print('\n')
# Varrendo dicionário por chave-valor
for chave, valor in carro.items():
    print(f'{chave} - {valor} (ok)')
print('\n')

print('\n' + 30*'#-' + '\n')  # Demarcador

# for com else - O else só é executado caso o break NÃO seja chamado no laço for
dias_uteis = ('segunda', 'terça', 'quarta', 'quinta', 'sexta')
dia_escolhido = 'domingo'

for dia in dias_uteis:
    if(dia_escolhido == dia):
        break
else:
    print(f'{dia_escolhido} não é considerado dia útil.')