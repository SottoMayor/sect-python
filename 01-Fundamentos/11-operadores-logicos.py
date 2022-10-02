'''
Lógicos: OR AND NOT IS IN
OR -> ou
AND -> e
NOT -> não (negação)
IS -> é
IN -> dentro

OBS: NOT, IS, IN também podem ser chamados de operadores de membros.
'''
# Aqui operamos com valores BOOLEANOS e o retorno é um BOOLEANO!
# É importante o entendimento da tabela verdade

sentenca_1 = 3 > 4 or 4 >= 4
sentenca_2 = 3 > 4 and 4 >= 4

# Leis de Morgan, usando operador relacional ==
lei_de_morgan_1 = not(sentenca_1) == (3 <= 4 and 4 < 4)
lei_de_morgan_2 = not(sentenca_2) == (3 <= 4 or 4 < 4)

print(sentenca_1)
print(sentenca_2)
print(lei_de_morgan_1)
print(lei_de_morgan_2)

# Operadores de membros
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(2 in numeros)
print(2 not in numeros)
print(10 not in numeros)

numeros_copia = numeros
outros_numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros_copia is numeros)
print(outros_numeros is numeros)
print(outros_numeros is not numeros)
# Isso acontece porque listas e dicionários apontam para o mesmo lugar
# da memoria, quando são atribuídos.
numeros_copia.pop()
print(numeros, numeros_copia, outros_numeros)

print('\n' + 30*'#-' + '\n')  # Demarcador

salario = 3500
despesas_mensais = 3349
promocao_cinema = True
# A conta só estará devedora caso as despesas sejam maior que o salario
dinheiro_sobrando = salario > despesas_mensais
ir_ao_cinema = dinheiro_sobrando and promocao_cinema
print(ir_ao_cinema)
