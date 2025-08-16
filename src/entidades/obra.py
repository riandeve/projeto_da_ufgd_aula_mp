from util.data import Data

obras = []

class Obra:
    def __init__(self, nome, localizacao, data_inicio, data_previsao_fim):
        self.nome = nome
        self.localizacao = localizacao
        self.data_inicio = data_inicio
        self.data_previsao_fim = data_previsao_fim

    def __str__(self):
        return f'{self.nome:<25} {self.localizacao:<20} Início: {str(self.data_inicio):<15} Fim: {str(self.data_previsao_fim):<15}'

def get_obras():
    return obras

def inserir_obra(obra):
    obras.append(obra)