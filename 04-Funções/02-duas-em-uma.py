'''
sintaxe...
def {function_name}({parameters}):
    ... código de execução
    return {function_return}
'''

# Combinar as funções fatorial e fatorial_duplo em uma só

# Estratégia 1- Definir as funções e usar uma 3° função para realizar a chamada


def fatorial_simples(num):
    if(num == 1 or num == 0):
        return 1
    sequencia_de_1_ao_num = range(1, num + 1)  # interável

    fatorial = 1
    for num_da_sequencia in sequencia_de_1_ao_num:
        fatorial *= num_da_sequencia

    return fatorial


def fatorial_duplo(num):
    if(num % 2 == 0):
        sequencia = range(2, num + 1, 2)  # interável
    else:
        sequencia = range(1, num + 1, 2)  # interável

    fatorial = 1
    for num_da_sequencia in sequencia:
        fatorial *= num_da_sequencia

    return fatorial


def fatorial_maneira_1(numero, duplo=False):  # Param OPCIONAL
    if(not duplo):
        return fatorial_simples(numero)
    else:
        return fatorial_duplo(numero)


print(fatorial_maneira_1(5))
print(fatorial_maneira_1(5, False))
print(fatorial_maneira_1(5, True))


print('\n' + 30*'#-' + '\n')  # Demarcador

# Estratégia 2- Criar uma função genérica que atenda a necessidade


def fatorial_maneira_2(numero, duplo=False):  # Param OPCIONAL
    if(numero % 2 == 0 and duplo):
        sequencia = range(2, numero + 1, 2)  # interável
    elif (numero % 2 != 0 and duplo):
        sequencia = range(1, numero + 1, 2)  # interável
    else:
        sequencia = range(1, numero + 1)

    fatorial = 1
    for num_da_sequencia in sequencia:
        fatorial *= num_da_sequencia

    return fatorial


print(fatorial_maneira_1(6))
print(fatorial_maneira_1(6, False))
print(fatorial_maneira_1(6, True))
