carro = {'marca': 'Hyundai', 'modelo': 'HB20',
         'autonomia': 12.5, 'gasolina_disponivel': 35, 'pneus': 93}
# OBS: autonomia em Km/L, gasolina_disponivel em L e pneus em %
# OBS: O carro a cada 15km o pneu perde 1% de vida útil.
# Não é possível rodar com menos de 35% de desgaste do pneu, nem se o carro não tiver mais gasolina

#  Quantos Km o carro consegue rodar, desconsiderando o desgaste dos pneus?
autonomia_gasolina = carro['autonomia'] * carro['gasolina_disponivel']
autonomia_pneu = round(carro['pneus'] - (autonomia_gasolina / 15), 2)
print(
    f'A autonomia de gasolina é de {autonomia_gasolina} km, o que garante {autonomia_pneu}% de autonomia de pneus.')

# Suponha que o a distância de uma cidade A para uma cidade B é de 300 km...
distancia = 250
print(f'Dados do carro antes da viagem: {carro}')

# Será se é possível ir de A e para B, considerando as restrições impostas?

# Atualizando os dados dentro do dicionário
carro['gasolina_disponivel'] -= round(distancia/carro['autonomia'], 2)
# carro['gasolina_disponivel'] = carro['gasolina_disponivel'] - round(distancia/carro['autonomia'], 2)
carro['pneus'] = autonomia_pneu

if(autonomia_gasolina >= distancia and autonomia_pneu > 35):
    print('Você conseguiu chegar à cidade B!')

if(carro['autonomia'] * carro['gasolina_disponivel'] > 150):
    print('Ainda é possível rodar mais de 150km com essa quantidade de gasolina restante.')

# Essa condicional é falsa!
if(carro['modelo'] == 'Creta'):
    print('O modelo de seu carro é um Creta!')

print(f'Dados do carro após a viagem: {carro}')
