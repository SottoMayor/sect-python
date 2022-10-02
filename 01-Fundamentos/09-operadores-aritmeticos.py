'''
Aritméticos: + - * ** / // %
+ -> soma
- -> subtração
* -> multiplicação
** -> exponenciação
/ -> divisão
// -> divisão inteira
% -> módulo ou resto da divisão.
'''

# Atenção toda operação com números float, resulta em um float.

soma = 1 + 2
subtracao = 1 - 2
multiplicacao = 5 * 2
exponenciacao = 5 ** 2  # pow(5,2) de forma alternativa
divisao = 10/3
divisao_inteira = 10//3
modulo = 10 % 2

print(soma)
print(subtracao)
print(multiplicacao)
print(exponenciacao)
print(divisao, round(divisao, 2))
print(divisao_inteira)
print(modulo)


print('\n' + 30*'#-' + '\n')  # Demarcador

salario = 3500
despesas_mensais = 3349
# A conta só estará devedora caso as despesas sejam maior que o salario
dinheiro_livre = salario - despesas_mensais
print(dinheiro_livre)
porc_salario_comprometido = (despesas_mensais * 100)/salario
print(porc_salario_comprometido, ' ', round(porc_salario_comprometido, 2))
