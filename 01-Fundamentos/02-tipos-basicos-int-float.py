# OBS números FLOAT são escritos com '.' e não com ','

inteiro = 12
flutuante = 1.5
negativo = -7
print('tipos', type(inteiro), type(flutuante), type(negativo))

# Toda operação de um número com um float, o resultado será float.
divisao = inteiro/flutuante
soma = inteiro + flutuante
print('divisao', divisao)
print('soma', soma)

# Podemos recuperar o valor absoluto de um número
absoluto = abs(negativo)
print('absoluto', absoluto)
print('absoluto flutuante', abs(flutuante))

# Arredondamento de um número.
quebrado = flutuante ** inteiro
quebrado_arredondado_2_casas = round(quebrado, 2)
print('quebrado', quebrado)
print('quebrado_arredondado_2_casas', quebrado_arredondado_2_casas)