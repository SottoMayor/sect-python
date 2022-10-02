# sintaxe -> { {key}: {value} for {item_list} in {list} if {condition} }

quadrados = {num: num**2 for num in range(0, 11)}  # sem condicional!
print(quadrados)

dobros_dos_impares = {f'{num} X 2': 2 *
                      num for num in range(0, 11) if num % 2 == 1}
print(dobros_dos_impares)

print('\n' + 30*'#-' + '\n')  # Demarcador

homens = {1: 'João', 2: 'Pedro', 3: 'Marcos', 4: 'Guilherme'}
mulheres = {1: 'Beatriz', 2: 'Antônia', 3: 'Gabriela', 4: 'Pâmela'}

casais = {homens[num]: mulheres[num] for num in range(1, 5)}
print(casais)

print('\n' + 30*'#-' + '\n')  # Demarcador

homens = {1: 'João', 2: 'Pedro', 3: 'Marcos', 4: 'Guilherme'}
mulheres = {1: 'Beatriz', 2: 'Antônia', 3: 'Gabriela', 4: 'Pâmela'}
filhos = {1: [], 2: ['Ana'], 3: ['Ronaldo', 'Felipe'], 4: []}

familia = {f'{homens[num]} e {mulheres[num]}': filhos[num]
           for num in range(1, 5)}
print(familia)
