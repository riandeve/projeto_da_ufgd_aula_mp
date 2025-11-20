equipamentos = {}

class Equipamento:
    def __init__(self, nome, tipo, valor, peso, disponivel):
        self.nome = nome
        self.tipo = tipo if tipo in (
            'Ferramenta Elétrica', 'Construção', 'Segurança',
            'Transporte', 'Medição', 'Corte', 'Elevação',
            'Movimentação de terra', 'Concretagem', 'Equipamentos de apoio'
        ) else 'indefinido'
        self.valor = valor
        self.peso = peso
        self.disponivel = disponivel

    def __str__(self):
        disponivel_str = 'disponível' if self.disponivel else ' '
        return f'{self.nome:<26} {self.tipo:<25} R$ {self.valor:<11.2f} {self.peso:<6}kg  {disponivel_str:>13} '


def get_equipamentos():
    return equipamentos


def inserir_equipamento(equipamento):
    nome = equipamento.nome
    if nome not in equipamentos:
        equipamentos[nome] = equipamento
    else:
        print(f'Equipamento {nome} já tem cadastro.')
