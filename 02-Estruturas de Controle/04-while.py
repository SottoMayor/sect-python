# Geralmente usamos o while quando queremos uma quantidade
# indefinida de iterações

acumuladora = 0  # Variável que acumula valores
contadora = 0  # Variável responsável para forçar a parada do laço

# Suponha que queremos fazer uma soma de todos os impares de 0 à 100
while(contadora <= 100):
    acumuladora += contadora
    # acumuladora = acumuladora + contadora

    contadora += 1

print(acumuladora)

print('\n' + 30*'#-' + '\n')  # Demarcador

# Podemos botar if dentro de laços também...

acumuladora = 1
contadora = 0

while(contadora < 15):
    acumuladora *= 2
    # acumuladora = acumuladora * 2

    if(acumuladora > 10000):
        print('MAIOR QUE 10000')

    print('acumuladora =', acumuladora)

    contadora += 1

print('\n' + 30*'#-' + '\n')  # Demarcador

# Cuidado! Se você não souber escrever a condição de parada ou esquecer de
# incrementar a variável contadora, podemos ter um laço infinito!

# contadora = 0
# while(contadora < 1): # Observe que essa condição nunca é alcançada!
#     print('Isso vai rodar pra sempre e indefinidademente!')

# print('\n' + 30*'#-' + '\n')  # Demarcador

# Break e Continue
# Break -> Força a parada do laço
# Continue -> Serve como um filtro, ou para pular uma iteração do laço

# Suponha um laço rodando em loop...
soma = 0
while(True):
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

# Adicionando elementos em uma lista usando uma laço
lista = []
contador = 0

print('lista antes do laço', lista)
while(contador < 5):
    lista.append(contador)

    contador += 1

print('lista após o laço', lista)

