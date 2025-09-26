from src.util.data import Data
from src.entidades.empreiteiro import Empreiteiro
from src.entidades.equipamento import get_equipamentos

obras = {}

class Obra:
    def __init__(self, id, descricao, data_inicio, empreiteiro=None):
        self.id = id
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim = None
        self.empreiteiro = empreiteiro
        self.equipamentos = {}

    def inserir_equipamento(self, equipamento):
        if equipamento.nome not in self.equipamentos:
            self.equipamentos[equipamento.nome] = equipamento

    def remover_equipamento(self, equipamento):
        chave = equipamento.nome
        if chave in self.equipamentos:
            del self.equipamentos[chave]
        else:
            print(f'Equipamento {chave} não está alocado na Obra {self.id}.')

    def listar_equipamentos(self):
        return self.equipamentos.values()

    def __str__(self):
        data_fim_str = str(self.data_fim) if self.data_fim else '---'
        empreiteiro_str = self.empreiteiro.nome if self.empreiteiro else '---'
        formato = '{:<12} {:<35} {:<12} {:<12} {:<25}'
        return formato.format(
            self.id,
            self.descricao[:34],
            str(self.data_inicio),
            data_fim_str,
            empreiteiro_str
        )

def get_obras():
    return obras

def inserir_obra(obra):
    id = obra.id
    if id  not in obras.keys():
        obras[id] = obra
    else:
        print(f'Obra {id} já tem cadastro.')
