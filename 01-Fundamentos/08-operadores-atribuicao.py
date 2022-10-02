'''
Atribuição: = += -= *= **= /= //= %=
= -> Atribuição
+= -> Atribuição com soma
-= -> Atruição com subtração
*= -> Atruição com multiplicação
**= -> Atruição com exponenciação
/= -> Atruição com divisão
//= -> Atruição com divisão inteira
%= -> Atruição com resto da divisão
'''
# A atribuicao é feita com o operador (=), básico!
nome = 'David'

# Agora, suponha que exista uma soma que inicia de 0 cresce de 5 em 5
soma = 0
print(soma)
soma = soma + 5
print(soma)
soma = soma + 5
print(soma)
soma = soma + 5
print(soma)
soma = soma + 5
print(soma)

print('\n')
# Nesse caso, chamamos soma de variável acumuladora.
# Para não ficar carregando a variável soma do lado direito da atruição podemos
# omití-la em uma sintaxe mais otimizada
soma = 0
print(soma)
soma += 5
print(soma)
soma += 5
print(soma)
soma += 5
print(soma)
soma += 5
print(soma)

print('\n' + 30*'#-' + '\n')  # Demarcador

# De maneira análoga para os outros tipos de operadores...
base_2 = 2
print(base_2)
base_2 = base_2 * 2
print(base_2)
base_2 = base_2 * 2
print(base_2)

print('\n')

base_2 = 2
print(base_2)
base_2 *= 2
print(base_2)
base_2 *= 2
print(base_2)