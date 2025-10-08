from src.entidades.obra import get_obras
from src.entidades.empreiteiro import get_empreiteiros
from src.entidades.equipamento import get_equipamentos
from src.util.data import Data

contratos = []

class Contrato:
    def __init__(self, obra, empreiteiro, equipamento, valor, data_assinatura, prazo):
        self.obra = obra
        self.empreiteiro = empreiteiro
        self.equipamento = equipamento
        self.valor = valor
        self.data_assinatura = data_assinatura
        self.prazo = prazo

    def __str__(self):
        formato = '{:<8} {:<25} {:<25} {:<25} {:<12} {:<15} {:<10}'
        return formato.format(
            self.obra.id,
            self.obra.descricao[:24],
            self.empreiteiro.nome[:24],
            self.equipamento.nome[:24],
            f'R$ {self.valor:.2f}',
            str(self.data_assinatura),
            f'{self.prazo} dias'
        )


def get_contratos():
    return contratos


def inserir_contrato(contrato):
    if contrato not in contratos:
        contratos.append(contrato)
    else:
        print('Contrato já cadastrado --- ' + str(contrato))


def get_contratos_obra(id_obra):
    contratos_obra = []
    for contrato in contratos:
        if contrato.obra.id == id_obra:
            contratos_obra.append(contrato)
    return contratos_obra


def criar_contrato(id_obra, nome_empreiteiro, nome_equipamento, valor, data_assinatura, prazo):
    obras = get_obras()
    empreiteiros = get_empreiteiros()
    equipamentos = get_equipamentos()

    if id_obra not in obras:
        print('Obra ' + str(id_obra) + ' não cadastrada')
        return
    if nome_empreiteiro not in empreiteiros:
        print('Empreiteiro ' + nome_empreiteiro + ' não cadastrado')
        return
    if nome_equipamento not in equipamentos:
        print('Equipamento ' + nome_equipamento + ' não cadastrado')
        return

    obra = obras[id_obra]
    empreiteiro = empreiteiros[nome_empreiteiro]
    equipamento = equipamentos[nome_equipamento]

    inserir_contrato(
        Contrato(obra, empreiteiro, equipamento, valor, data_assinatura, prazo)
    )
