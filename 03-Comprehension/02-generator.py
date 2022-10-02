# sintaxe -> ( {expression} for {list_item} in {list} if {condition} )

# OBS: O generator é mais econômico que o list comprehension, em questão de
# memória. O generator é gerado sob demanda, por isso usamos a func next()

quadrados = (num**2 for num in range(0, 5))  # sem condicional!
print(quadrados)  # print do generator em si
print(next(quadrados))  # 0
print(next(quadrados))  # 1
print(next(quadrados))  # 2
print(next(quadrados))  # 3
print(next(quadrados))  # 4
# print(next(quadrados)) # Erro

print('\n' + 30*'#-' + '\n')  # Demarcador

# Podemos usar o generator com um laço, sem dificuldade
quadrados = (num**2 for num in range(0, 5))  # sem condicional!

for quadrado in quadrados:  # quadrados é um generator
    print(f'{quadrado ** (1/2)} de eh {quadrado}')
