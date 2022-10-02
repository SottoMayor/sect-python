'''
Dada 2 sentenças A e B, e uma condição COND, temos:

Ternários:
Maneira 1 -> (B, A)[COND]
Maneira 2 -> A if COND else B
'''
salario = 3500
despesas_mensais = 3349
promocao_cinema = True
# A conta só estará devedora caso as despesas sejam maior que o salario
dinheiro_sobrando = salario > despesas_mensais
ir_ao_cinema = dinheiro_sobrando and promocao_cinema

retorno_mensagem = ('Ops... é melhor ir ao cinema outro dia.',
                    'EBA! Hoje é dia de ver um filme!', )[ir_ao_cinema]
print('ir_ao_cinema', ir_ao_cinema)
print(retorno_mensagem)

# retorno_inteiro é 1 caso dinheiro_sobrando seja True senão é 0
retorno_inteiro = 1 if dinheiro_sobrando else 0
print(retorno_inteiro)
