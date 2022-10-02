from random import randint

# Suponha que você está apostando no jogo do bicho

'''
1 Avestruz. 2 Águia. 3 Burro. 4 Borboleta. 5 Cachorro. 6 Cabra. 7 Carneiro.
8 Camelo. 9 Cobra. 10 Coelho. 11 Cavalo. 12 Elefante. 13 Galo. 14 Gato.
15 Jacaré 16 Leão. 17 Macaco. 18 Porco. 19 Pavão. 20 Peru. 21 Touro.
22 Tigre. 23 Urso. 24 Veado. 25 Vaca.
'''

numero_bicho_escolhido = 10
sorteio = randint(1, 30)

if(sorteio == 1):
    print('Avestruz')
elif(sorteio == 2):
    print('Águia')
elif(sorteio == 3):
    print('Burro')
elif(sorteio == 4):
    print('Borboleta')
elif(sorteio == 5):
    print('Cachorro')
elif(sorteio == 6):
    print('Cabra')
elif(sorteio == 7):
    print('Carneiro')
elif(sorteio == 8):
    print('Camelo')
elif(sorteio == 9):
    print('Cobra')
elif(sorteio == 10):
    print('Coelho')
elif(sorteio == 11):
    print('Cavalo')
elif(sorteio == 12):
    print('Elefante')
elif(sorteio == 13):
    print('Galo')
elif(sorteio == 14):
    print('Gato')
elif(sorteio == 15):
    print('Jacaré')
elif(sorteio == 16):
    print('Leão')
elif(sorteio == 17):
    print('Macaco')
elif(sorteio == 18):
    print('Porco')
elif(sorteio == 19):
    print('Pavão')
elif(sorteio == 20):
    print('Peru')
elif(sorteio == 21):
    print('Touro')
elif(sorteio == 22):
    print('Tigre')
elif(sorteio == 23):
    print('Urso')
elif(sorteio == 24):
    print('Veado')
elif(sorteio == 25):
    print('Vaca')
else:
    print(f'O número {sorteio} não é válido no jogo do bicho.')

mensagem = 'Você ganhou!' if numero_bicho_escolhido == sorteio else 'Você perdeu :('
print(mensagem)
