from util.gerais import imprimir_objetos
from util.data import Data
from entidades.equipamento import Equipamento, inserir_equipamento, get_equipamentos
from entidades.empreiteiro import Empreiteiro, inserir_empreiteiro, get_empreiteiros
from entidades.obra import Obra, inserir_obra, get_obras


def cadastrar_equipamentos():
    inserir_equipamento(Equipamento('Betoneira', 'betoneira', 150.00, True))
    inserir_equipamento(Equipamento('Furadeira', 'furadeira', 75.50, False))
    inserir_equipamento(Equipamento('Serra', 'serra', 120.00, True))
    inserir_equipamento(Equipamento('Martelo', 'martelo', 250.00, True))


def cadastrar_empreiteiros():
    inserir_empreiteiro(
        Empreiteiro('Construções Rian Ltda.', '(67) 9999-8888', 'contato@gmail.com', 'Rua dos Pedreiros, 123'))
    inserir_empreiteiro(Empreiteiro('Serviços Mestre', '(67) 8888-7777', 'mestre@gmail.com', 'Avenida da Obra, 456'))
    inserir_empreiteiro(Empreiteiro('Construção Civil G-3', '(67) 7777-6666', 'contato@gmail.com', 'Rua da Inovação, 789'))


def cadastrar_obras():
    inserir_obra(Obra('Residencial Solar', 'Rua das Flores, 100', Data(10, 8, 2025), Data(10, 12, 2025)))
    inserir_obra(Obra('Comercial Alfa', 'Avenida Principal, 500', Data(1, 9, 2025), Data(1, 3, 2026)))
    inserir_obra(Obra('Praça do Sol Nascente', 'Praça Central', Data(20, 7, 2025), Data(20, 10, 2025)))


def executar():
    print('\n----- PROJETO: Alocacao de Equipamentos da Construcao Civil -----')

    cadastrar_equipamentos()
    imprimir_objetos('EQUIPAMENTOS', get_equipamentos())

    cadastrar_empreiteiros()
    imprimir_objetos('EMPREITEIROS', get_empreiteiros())

    cadastrar_obras()
    imprimir_objetos('OBRAS', get_obras())