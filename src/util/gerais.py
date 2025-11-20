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


def ordenar_objetos_por_um_atributo(objetos, atributo, ordenação_decrescente):
    objetos_ordenados = list(objetos)
    objetos_ordenados.sort(key=atributo, reverse=ordenação_decrescente)
    return objetos_ordenados


def ordenar_objetos_por_dois_atributos(objetos, atributo1, atributo2, ordenação_decrescente):
    objetos_ordenados_atributo1 = list(objetos)
    objetos_ordenados_atributo1.sort(key=atributo1, reverse=ordenação_decrescente)
    objetos_ordenados_atributo1_atributo2 = []
    último_atributo1 = atributo1(objetos_ordenados_atributo1[0])
    objetos_mesmo_atributo1 = []

    for objeto in objetos_ordenados_atributo1:
        if atributo1(objeto) == último_atributo1:
            objetos_mesmo_atributo1.append(objeto)
        else:
            objetos_mesmo_atributo1.sort(key=atributo2, reverse=ordenação_decrescente)
            for objeto_mesmo_atributo1 in objetos_mesmo_atributo1:
                objetos_ordenados_atributo1_atributo2.append(objeto_mesmo_atributo1)
            objetos_mesmo_atributo1 = [objeto]
            último_atributo1 = atributo1(objeto)

    objetos_mesmo_atributo1.sort(key=atributo2, reverse=ordenação_decrescente)
    for objeto_mesmo_atributo1 in objetos_mesmo_atributo1:
        objetos_ordenados_atributo1_atributo2.append(objeto_mesmo_atributo1)

    return objetos_ordenados_atributo1_atributo2
