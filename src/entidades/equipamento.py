equipamentos = []

class Equipamento:
    def __init__(self, nome, tipo, valor_diaria, disponivel):
        self.nome = nome
        self.tipo = tipo if tipo in ('betoneira', 'furadeira', 'serra', 'martelo') else 'indefinido'
        self.valor_diaria = valor_diaria
        self.disponivel = disponivel

    def __str__(self):
        disponivel_str = 'disponível' if self.disponivel else ''
        return f'{self.nome:<25} {self.tipo:<25} R$ {self.valor_diaria:<10.2f} {disponivel_str:<15}'

def get_equipamentos():
    return equipamentos

def inserir_equipamento(equipamento):
    equipamentos.append(equipamento)