empreiteiros = {}

class Empreiteiro:
    def __init__(self, nome, telefone, email, endereço):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereço = endereço

    def __str__(self):
        return f'{self.nome:<30} {self.telefone:<20} {self.email:<30} {self.endereço:<25}'

def get_empreiteiros():
    return empreiteiros

def inserir_empreiteiro(empreiteiro):
    nome = empreiteiro.nome
    if nome not in empreiteiros.keys():
        empreiteiros[nome] = empreiteiro
    else:
        print(f'Empreiteiro {nome} já tem cadastro.')