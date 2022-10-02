# Gere uma lista (lista_a) de números ímpares de 1 à 50
# Gere uma lista (lista_b) de múltiplos de 3 de 1 à 20
# Gere uma lista em que contenha todos os elementos da lista_a e lista_b

lista_a = [num for num in range(1, 51) if num % 2 == 1]
lista_b = [3*num for num in range(1, 21)]

lista_final = [num for num in lista_a if num in lista_b]

print(lista_a)
print(lista_b)
print(lista_final)
