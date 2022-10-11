def unicos(*args, **kwargs):

    retorna_lista = kwargs.get('retorna_lista', True)

    dicionario_contagem = {}
    for elemento in args:
        if elemento in dicionario_contagem:
            dicionario_contagem[elemento] += (dicionario_contagem[elemento])
        else:
            dicionario_contagem[elemento] = 1
    print(dicionario_contagem)

    lista_chaves_dicionario_contagem = [
        chave for chave in dicionario_contagem.keys()
    ]

    if(retorna_lista):
        return lista_chaves_dicionario_contagem
    else:
        return 'O retorno da lista está desabilitado!'


print(
    unicos('David', 'David', 'David', 'Sotto', 'Mayor', 'Sotto', 'Matemática')
)
