'''
sintaxe...
def {function_name}({parameters}):
    ... código de execução
    return {function_return}
'''

# Função fatorial -> n! = n*(n-1)*(n-2)...*3*2*1


def fatorial(num):  # Parâmetro
    if(num == 1 or num == 0):
        return 1
    sequencia_de_1_ao_num = range(1, num + 1)  # interável

    fatorial = 1
    for num_da_sequencia in sequencia_de_1_ao_num:
        fatorial *= num_da_sequencia

    # print(fatorial)

    return fatorial


# invocando a função
fatorial_5 = fatorial(5)  # Argumento
print(fatorial_5)
print(fatorial(0))

print('\n' + 30*'#-' + '\n')  # Demarcador

# Agora vamos fazer uma função fatorial duplo
# Fatorial duplo -> n!! = n*(n-2)*(n-4)*...*4*2


def fatorial_duplo(num):
    if(num % 2 == 0):
        sequencia = range(2, num + 1, 2)  # interável
    else:
        sequencia = range(1, num + 1, 2)  # interável

    fatorial = 1
    for num_da_sequencia in sequencia:
        # print(num_da_sequencia)
        fatorial *= num_da_sequencia

    # print(fatorial)

    return fatorial


print(fatorial_duplo(5))
