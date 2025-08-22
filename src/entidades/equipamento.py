equipamentos = []

class Equipamento:
    def __init__(self, nome, tipo, valor, disponivel):
        self.nome = nome
        self.tipo = tipo if tipo in ('Ferramenta Elétrica', 'Construção', 'Segurança', 'Transporte', 'Medição', 'Corte', 'Elevação') else 'indefinido'
        self.valor = valor
        self.disponivel = disponivel

    def __str__(self):
        disponivel_str = 'disponível' if self.disponivel else ''
        return f'{self.nome:<25} {self.tipo:<25} R$ {self.valor:<10.2f} {disponivel_str:<15}'

def get_equipamentos():
    return equipamentos

def inserir_equipamento(equipamento):
    equipamentos.append(equipamento)