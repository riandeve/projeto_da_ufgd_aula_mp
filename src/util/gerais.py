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

def ordenar_objetos_por_um_atributo(objetos, comparador):
    objetos_ordenados = []
    for objeto_desordenado in objetos:
        ordenou_objeto = False
        for indice, objeto_ordenado in enumerate(objetos_ordenados):
            if comparador(objeto_desordenado, objeto_ordenado):
                objetos_ordenados.insert(indice, objeto_desordenado)
                ordenou_objeto = True
                break
        if not ordenou_objeto:
            objetos_ordenados.append(objeto_desordenado)
    return objetos_ordenados