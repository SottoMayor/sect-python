from random import randint

# Suponha que você quer ir num rodízio de R$ 40, mas só tem R$10, então você
# decide fazer um betting no mengão mavaldão.

# REGRA DO BETTING: Você ganha se cair um número par, e o dinheiro a
# ser recebido é a quantidade apostada vezes o número sorteado

# REGRA DO RODÍZIO: Você só vai ao rodízio se tiver pelo menos R$40

valor_recebido = 0
valor_rodizio = 40
valor_aposta = 10
ganhou = False

numero_betting = randint(0, 10)  # par o flamengo ganha, ímpar perde
print(f'O número sorteado foi: {numero_betting}')

# O número sorteado é par?
if(numero_betting % 2 == 0 and numero_betting != 0):
    ganhou = True  # Flag

    print('Você ganhou no betting!')
    valor_recebido = valor_aposta * numero_betting
    print(f'Agora você tem R${valor_recebido}')
    if(valor_recebido >= valor_rodizio):
        print(
            f'Você conseguiu a grana do rodízio! R${valor_recebido} na carteira')
    else:
        print(
            f'Apesar de ter ganhado o betting, você não vai ao rodízio! R${valor_recebido} não conseguem pagar um rodízio de R${valor_rodizio}')
else:
    print('Você perdeu o betting! Agora está liso e com fome hahaha')

# O código abaixo vai executar apenas após a estrutura condicional ser executada
if(ganhou):
    print('Adoro fazer apostas no mengão!!!!')
else:
    print('Flamengo só decepciona, nunca mais aposto nada!')

perdeu_ou_ganhou = ('perdeu', 'ganhou')[ganhou]  # ternário
# perdeu_ou_ganhou = 'ganhou' if ganhou else 'perdeu'  # ternário

print(
    f'Resultado: você apostou R${valor_aposta}, o flamengo {perdeu_ou_ganhou} e agora você tem R$ {valor_recebido}')
