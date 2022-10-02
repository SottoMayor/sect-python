'''
Relacionais: == != > < >= <=
== -> Igual
!= -> Diferente
> -> Maior que
< ->  Menor que
>= -> Maior ou igual que
<= -> Menor ou igual que
'''

# Atenção! Esse tipo de operador retorna um valor BOOLEANO (V ou F)

print(3 > 4)
print(10 >= 10)
print(10 <= 10)
print(10 != 10)
print(10 != '10')

print('\n' + 30*'#-' + '\n')  # Demarcador

salario = 3500
despesas_mensais = 3349
# A conta só estará devedora caso as despesas sejam maior que o salario
nao_devo_ninguem = salario >= despesas_mensais
print(nao_devo_ninguem)
