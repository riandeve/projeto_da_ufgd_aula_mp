from src.util.gerais import imprimir_objetos, ordenar_objetos_por_um_atributo
from src.util.data import Data
from src.entidades.empreiteiro import Empreiteiro, get_empreiteiros, inserir_empreiteiro
from src.entidades.equipamento import Equipamento, get_equipamentos, inserir_equipamento
from src.entidades.obra import Obra, get_obras, inserir_obra
from src.entidades.equipamento import get_equipamentos
from src.entidades.contrato import criar_contrato, get_contratos, get_contratos_obra
from src.util.gerais import ordenar_objetos_por_um_atributo, ordenar_objetos_por_dois_atributos
from src.util.data import Data





def cadastrar_equipamentos():
    inserir_equipamento(Equipamento("Furadeira", "Ferramenta Elétrica", 20, False))
    inserir_equipamento(Equipamento("Lixadeira", "Ferramenta Elétrica", 18, True))
    inserir_equipamento(Equipamento("Betoneira", "Construção", 320, False))
    inserir_equipamento(Equipamento("Andaime", "Construção", 200, True))
    inserir_equipamento(Equipamento("Capacete de proteção", "Segurança", 1, False))
    inserir_equipamento(Equipamento("Cinto de segurança", "Segurança", 3, False))
    inserir_equipamento(Equipamento("Carrinho de mão", "Transporte", 15, True))
    inserir_equipamento(Equipamento("Empilhadeira", "Transporte", 3500, True))
    inserir_equipamento(Equipamento("Trena", "Medição", 0.5, False))
    inserir_equipamento(Equipamento("Nível a laser", "Medição", 2, True))
    inserir_equipamento(Equipamento("Serra circular", "Corte", 12, False))
    inserir_equipamento(Equipamento("Esmerilhadeira", "Corte", 8, True))
    inserir_equipamento(Equipamento("Guincho", "Elevação", 500, True))
    inserir_equipamento(Equipamento("Talha manual", "Elevação", 50, False))


def cadastrar_empreiteiros():
    inserir_empreiteiro(Empreiteiro("Construções Dourados Ltda.", "(67) 9999-8888",
                                    "contato.dourados@gmail.com", "Rua dos Pedreiros, 123"))
    inserir_empreiteiro(Empreiteiro("Serviços de Telecomunicação", "(67) 8888-7777",
                                    "tele.servicos@gmail.com", "Avenida da Obra, 456"))
    inserir_empreiteiro(Empreiteiro("Construção Civil", "(67) 7777-6666",
                                    "contato.g3@gmail.com", "Rua da Inovação, 789"))


def cadastrar_obras():
    empreiteiros = get_empreiteiros()
    equipamentos = get_equipamentos()

    obra1 = Obra(837, "Construção do Edifício Sol", Data(2, 3, 2023),
                 empreiteiro=empreiteiros["Construções Dourados Ltda."])
    for nome_eq in ["Betoneira", "Andaime", "Guincho", "Furadeira"]:
        obra1.inserir_equipamento(equipamentos[nome_eq])
    inserir_obra(obra1)

    obra2 = Obra(524, "Reforma da Escola Municipal", Data(15, 4, 2023),
                 empreiteiro=empreiteiros["Serviços de Telecomunicação"])
    for nome_eq in ["Lixadeira", "Capacete de proteção", "Cinto de segurança", "Nível a laser"]:
        obra2.inserir_equipamento(equipamentos[nome_eq])
    inserir_obra(obra2)

    obra3 = Obra(796, "Shopping novo da cidade", Data(16, 9, 2024),
                 empreiteiro=empreiteiros["Construção Civil"])
    for nome_eq in ["Carrinho de mão", "Trena", "Guincho"]:
        obra3.inserir_equipamento(equipamentos[nome_eq])
    inserir_obra(obra3)

def cadastrar_contratos():
    criar_contrato(837, "Construções Dourados Ltda.", "Betoneira", 50000, Data(1, 5, 2023), 90)
    criar_contrato(837, "Construções Dourados Ltda.", "Andaime", 25000, Data(1, 5, 2023), 90)
    criar_contrato(524, "Serviços de Telecomunicação", "Nível a laser", 15000, Data(10, 6, 2023), 60)
    criar_contrato(524, "Serviços de Telecomunicação", "Cinto de segurança", 3000, Data(10, 6, 2023), 60)
    criar_contrato(796, "Construção Civil", "Carrinho de mão", 12000, Data(15, 7, 2024), 120)
    criar_contrato(796, "Construção Civil", "Guincho", 50000, Data(15, 7, 2024), 120)


if __name__ == '__main__':
    cadastrar_equipamentos()
    cadastrar_empreiteiros()
    cadastrar_obras()
    cadastrar_contratos()

    imprimir_objetos('Obra : id, descrição, datas, empreiteiro', get_obras().values())
    imprimir_objetos('Empreiteiros: nome, telefone, email, endereço', get_empreiteiros().values())
    imprimir_objetos('Contratos: id, valor, data_assinatura, obra, empreiteiro', get_contratos())

    for obra in get_obras().values():
        print('\n\n=== ' + obra.descricao + ' ===')

        equipamentos_obra = obra.listar_equipamentos()
        imprimir_objetos('Equipamento : nome, tipo, valor, status', equipamentos_obra)

        equipamentos_ordenados = ordenar_objetos_por_um_atributo(
            objetos=equipamentos_obra,
            comparador=lambda e1, e2: (e1.valor > e2.valor)
        )
        imprimir_objetos(
            'Equipamento : nome, tipo, valor, status -- Valor ordenado',
            equipamentos_ordenados
        )
    print('\n\n=== Contratos por Obra ===')
    for obra in get_obras().values():
        print('\nObra:', obra.descricao)
        contratos_obra = get_contratos_obra(obra.id)
        imprimir_objetos('Contrato : obra, empreiteiro, equipamento, valor, data, prazo', contratos_obra)

        contratos_ordenados_valor = ordenar_objetos_por_um_atributo(
            objetos=contratos_obra,
            comparador=lambda c1, c2: c1.valor > c2.valor
        )

        imprimir_objetos('Contratos -- ordem decrescente de valor', contratos_ordenados_valor)

        contratos_ordenados_dois = ordenar_objetos_por_dois_atributos(
            objetos=contratos_obra,
            atributo1=lambda c: c.valor,
            atributo2=lambda c: c.prazo,
            ordenação_decrescente=True
        )

        imprimir_objetos('Contratos -- ordem decrescente de valor e prazo', contratos_ordenados_dois)
