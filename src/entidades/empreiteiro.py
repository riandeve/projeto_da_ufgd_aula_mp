empreiteiros = []

class Empreiteiro:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self):
        return f'{self.nome:<25} {self.telefone:<15} {self.email:<30} {self.endereco:<25}'

def get_empreiteiros():
    return empreiteiros

def inserir_empreiteiro(empreiteiro):
    empreiteiros.append(empreiteiro)