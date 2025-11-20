from src.entidades.obra import get_obras
from src.entidades.empreiteiro import get_empreiteiros
from src.entidades.equipamento import get_equipamentos
from src.util.data import Data

contratos = []

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

    inserir_contrato(
        Contrato(
            obras[id_obra],
            empreiteiros[nome_empreiteiro],
            equipamentos[nome_equipamento],
            valor,
            data_assinatura,
            prazo
        )
    )

class Contrato:
    contador_id = 1
    def __init__(self, obra, empreiteiro, equipamento, valor, data_assinatura, prazo):
        self.id = Contrato.contador_id
        Contrato.contador_id += 1
        self.obra = obra
        self.empreiteiro = empreiteiro
        self.equipamento = equipamento
        self.valor = valor
        self.data_assinatura = data_assinatura
        self.prazo = prazo

    def __str__(self):
        formato = '{:<31} {:<29} {:<22} R$ {:<12.2f} {:<14} {:<10}'
        return formato.format(
            self.obra.descricao[:30],
            self.empreiteiro.nome[:25],
            self.equipamento.nome[:20],
            self.valor,
            str(self.data_assinatura),
            f'{self.prazo} dias'
        )
