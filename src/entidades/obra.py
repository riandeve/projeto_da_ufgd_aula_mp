from src.util.data import Data
from src.entidades.empreiteiro import Empreiteiro
from src.entidades.equipamento import get_equipamentos

obras = {}

class Obra:
    def __init__(self, id, descrição, data_inicio: Data, data_fim: Data = None, empreiteiro: Empreiteiro = None):
        self.id = id
        self.descrição = descrição
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.empreiteiro = empreiteiro
        self.equipamentos = {}

    def inserir_equipamentos(self, chaves_equipamentos):
        for chave_equipamento in chaves_equipamentos:
            if chave_equipamento in get_equipamentos().keys():
                self.equipamentos[chave_equipamento] = get_equipamentos()[chave_equipamento]
            else:
                print(f'Equipamento {chave_equipamento} não tem cadastro.')

    def remover_equipamento(self, equipamento):
        chave = equipamento.nome
        if chave in self.equipamentos:
            del self.equipamentos[chave]
        else:
            print(f'Equipamento {chave} não está alocado na Obra {self.id}.')

    def listar_equipamentos(self):
        return list(self.equipamentos.values())

    def __str__(self):
        data_fim_str = str(self.data_fim) if self.data_fim else '---'
        empreiteiro_str = self.empreiteiro.nome if self.empreiteiro else '---'
        formato = '{:<12} {:<35} {:<12} {:<12} {:<25}'
        return formato.format(self.id, self.descrição[:34], str(self.data_inicio), data_fim_str, empreiteiro_str)

def get_obras():
    return obras

def inserir_obra(obra):
    id_obra = obra.id
    if id_obra not in obras.keys():
        obras[id_obra] = obra
    else:
        print(f'Obra {id_obra} já tem cadastro.')