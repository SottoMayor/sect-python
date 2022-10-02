# Além disso, podemos criar laços aninhados (um dentro do outro).
# Podemos enxergar essa arrumação como uma matriz.

# Os laços aninhados rodam um seguido do outro. O laço de fora só dá
# uma iterada quando o laço de dentro completa todas as interadas.

for _ in range(3):
    print('[fora]')
    for _ in range(3):
        print('...dentro...')

# Montando uma Tabuada...
for linha in range(1, 11):
    for coluna in range(1, 11):
        print(f'{linha} X {coluna} = {linha * coluna}')