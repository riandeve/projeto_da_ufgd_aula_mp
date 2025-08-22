def compacta_nome(nome):
    partes_nome = nome.split(' ')
    nome_compactado = ''
    for parte_nome in partes_nome:
        nome_compactado += parte_nome if parte_nome not in ('de', 'da', 'das', 'do', 'dos') else ''
    return nome_compactado
def imprimir_objetos(cabeçalho, objetos):
    print('\n' + cabeçalho)
    for indice, objeto in enumerate(objetos):
        formato = '{:<5} {}'
        print(formato.format(str(indice + 1) + ' -', str(objeto)))

