from util.gerais import imprimir_objetos
from util.data import Data
from entidades.empreiteiro import Empreiteiro, inserir_empreiteiro, get_empreiteiros
from entidades.equipamento import Equipamento, inserir_equipamento, get_equipamentos

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
    inserir_empreiteiro(Empreiteiro("Construções Dourados Ltda.", "(67) 9999-8888", "contato.dourados@gmail.com", "Rua dos Pedreiros, 123"))
    inserir_empreiteiro(Empreiteiro("Serviços de Telecomunicação", "(67) 8888-7777", "tele.servicos@gmail.com", "Avenida da Obra, 456"))
    inserir_empreiteiro(Empreiteiro("Construção Civil", "(67) 7777-6666", "contato.g3@gmail.com", "Rua da Inovação, 789"))

if __name__ == '__main__':
    print('\nAlocação de Equipamentos da Construção Civil')
    cadastrar_equipamentos()
    imprimir_objetos('Equipamento: nome, tipo, valor, disponível', get_equipamentos())
    cadastrar_empreiteiros()
    imprimir_objetos('Empreiteiro: nome, telefone, email, endereço', get_empreiteiros())
