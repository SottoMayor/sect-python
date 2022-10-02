# sintaxe -> [ {expression} for {list_item} in {list} if {condition} ]

pares = [num for num in range(0, 11) if num % 2 == 0]
print(pares)

quadrados = [num**2 for num in range(0, 11)]  # sem condicional!
print(quadrados)

print('\n' + 30*'#-' + '\n')  # Demarcador

# Adicionando dados com list comprehension vs laço de repetição

impares_comp = [2*num + 1 for num in range(0, 10) if num % 2 == 1]
print(impares_comp)

impares_laco = []
for num in range(0, 10):
    if(num % 2 == 1):
        impares_laco.append(2*num + 1)
print(impares_laco)

print('\n' + 30*'#-' + '\n')  # Demarcador

# Resolvendo o desafio do arquivo '07-desafio-2.py' em '02-Estruturas de
# Controle' usando list comprehension...

# Entre com um número e devolva uma lista com seus divisores

# Divisor -> Um número é divisor do outro quando temos uma divisão
# exata, ou seja, quando ela não deixa resto.

# Dica: use um range de (1, n), onde p é o número de entrada

# Bônus: Verifique se o número de entrada é primo

numero = 7

divisores = [divisor for divisor in range(
    1, numero + 1) if numero % divisor == 0]

print(f'lista com os divisores de {numero}: {divisores}')

# Verificando se o número de entrada é primo
if(len(divisores) == 2):
    print(f'{numero} é primo.')
else:
    print(f'{numero} não é primo.')
