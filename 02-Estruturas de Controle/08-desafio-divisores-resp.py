# Entre com um número e devolva uma lista com seus divisores

# Divisor -> Um número é divisor do outro quando temos uma divisão
# exata, ou seja, quando ela não deixa resto.

# Dica: use um range de (1, n), onde p é o número de entrada

# Bônus: Verifique se o número de entrada é primo


numero = 20
lista = []

for divisor in range(1, numero + 1):
    if(numero % divisor == 0):
        lista.append(divisor)

print(f'lista com os divisores de {numero}: {lista}')

# Verificando se o número de entrada é primo
if(len(lista) == 2):
    print(f'{numero} é primo.')
else:
    print(f'{numero} não é primo.')
