# Entre com um número e verifique se ele é primo

# Números Primos -> Chamamos de número primo um número natural que possui dois
# divisores: 1 e ele mesmo.

# Dica: use um range de (1, n), onde n é o número de entrada

numero = 10
eh_primo = True

for divisor in range(1, numero + 1):
    print('divisor - ', divisor, '-> numero % divisor ', numero % divisor)

    # Entrar no condicional se...
    if(divisor != 1 and divisor != numero and numero % divisor == 0):
        eh_primo = False
        break

if(eh_primo):
    print(f'{numero} é primo')
else:
    print(f'{numero} não é primo')
