# Com operador * agrupa params posicionais, em forma de TUPLA, dentro da
# variável args

# Função de soma de dois números
def soma_2_numeros(a, b):
    return a + b


print(soma_2_numeros(1, 2))


# Função de soma de três números


def soma_3_numeros(a, b, c):
    return a + b + c


print(soma_3_numeros(1, 2, 3))

# Se eu quiser somar n números, como proceder????!
# Para isso usamos *args!


def soma_n_numeros(*args):
    tupla_de_numeros = args  # mais clareza que é uma tupla

    soma = 0
    for numero in tupla_de_numeros:
        soma += numero

    return soma


print(soma_n_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9))


print('\n' + 30*'#-' + '\n')  # Demarcador

# Faça uma função que recebe uma lista de números e uma série de números como
# parâmetros. Retorne a lista, sem os números que foram passados como
# parâmetros.


def limpador_de_lista(lista, *args):
    if(len(lista) == 0):
        return []

    tupla_de_numeros = args  # mais clareza que é uma tupla

    # Vamos varrer a lista e retirar número que está na tupla_de_numeros
    lista_limpa = [num for num in lista if num not in tupla_de_numeros]

    # Alternativamente, sem list comprehension...
    # lista_limpa = []
    # for num in lista:
    #     if(num not in tupla_de_numeros):
    #         lista_limpa.append(num)

    return lista_limpa


print(limpador_de_lista([1, 2, 3, 4, 5], 4, 5, 6))
print(limpador_de_lista([], 4, 5, 6))
