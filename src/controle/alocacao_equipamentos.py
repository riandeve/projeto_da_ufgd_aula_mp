from src.util.gerais import imprimir_objetos, ordenar_objetos_por_um_atributo
from src.util.data import Data
from src.entidades.empreiteiro import Empreiteiro, get_empreiteiros, inserir_empreiteiro
from src.entidades.equipamento import Equipamento, get_equipamentos, inserir_equipamento
from src.entidades.obra import Obra, get_obras, inserir_obra


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
    obra1.inserir_equipamentos(["Betoneira", "Andaime", "Guincho", "Furadeira"])
    inserir_obra(obra1)


    obra2 = Obra(524, "Reforma da Escola Municipal", Data(15, 4, 2023),
                 empreiteiro=empreiteiros["Serviços de Telecomunicação"])
    obra2.inserir_equipamentos(["Lixadeira", "Capacete de proteção", "Cinto de segurança", "Nível a laser"])
    inserir_obra(obra2)


    obra3 = Obra(796, "Shopping novo da cidade", Data(16, 9,2024),
                empreiteiro=empreiteiros["Construção Civil"])
    obra3.inserir_equipamentos(["Carrinho de mão", "Trena","Guincho"])
    inserir_obra(obra3)


if __name__ == '__main__':
    print('\nAlocação de Equipamentos da Construção Civil')

    cadastrar_equipamentos()
    imprimir_objetos('Equipamento: nome, tipo, valor, disponível', get_equipamentos().values())

    cadastrar_empreiteiros()
    imprimir_objetos('Empreiteiro: nome, telefone, email, endereço', get_empreiteiros().values())

    cadastrar_obras()
    imprimir_objetos('Obra: id, descrição, datas e empreiteiro', get_obras().values())

    print("\nEquipamentos ordenados por valor (decrescente):")
    equipamentos_ordenados = ordenar_objetos_por_um_atributo(
        objetos=get_equipamentos().values(),
        comparador=lambda e1, e2: e1.valor > e2.valor
    )
    imprimir_objetos('Equipamento: nome, tipo, valor, disponível', equipamentos_ordenados)

    print("\nEmpreiteiros ordenados por valor (decrescente):")
    empreiteiro_ordenados = ordenar_objetos_por_um_atributo(
        objetos=get_empreiteiros().values(),
        comparador=lambda e1, e2: e1.nome > e2.nome
    )
    imprimir_objetos('Empreiteiro: nome, telefone, email, endereço', empreiteiro_ordenados)