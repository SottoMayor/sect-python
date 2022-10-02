# o dicionário filmes_notas possui em suas chaves filmes e em seus respectivos 
# valores  são suas notas

# Gerar um novo dicionário que tenha apenas filmes que tenham notas maiores 
# que 9.2; em que o filme é a chave e a nota é o valor

filmes_notas = {"Veloses e Furiosos": 8.5, "Avatar": 9.1,
                "Bastardos Inglórios": 10, "Vingadores": 9.2, 'Interestrelar': 9.4}
filmes_notas_filtro = {key: value for key,
                       value in filmes_notas.items() if value > 9.2}


print(filmes_notas_filtro)
