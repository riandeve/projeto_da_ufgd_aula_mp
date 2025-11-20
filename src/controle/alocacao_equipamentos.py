import json
import os
from src.util.data import Data
from src.entidades.empreiteiro import Empreiteiro, inserir_empreiteiro, get_empreiteiros
from src.entidades.equipamento import Equipamento, inserir_equipamento, get_equipamentos
from src.entidades.obra import Obra, inserir_obra, get_obras
from src.entidades.contrato import criar_contrato
from src.interface.interface_textual import run_interface


def carregar_objetos_arquivo(caminho_arquivo):
    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    for e in dados["empreiteiros"]:
        inserir_empreiteiro(Empreiteiro(e["nome"], e["telefone"], e["email"], e["endereco"]))

    for eq in dados["equipamentos"]:
        inserir_equipamento(Equipamento(eq["nome"], eq["tipo"], eq["valor"], eq["peso"], eq["disponivel"]))

    empreiteiros = get_empreiteiros()
    equipamentos = get_equipamentos()

    for o in dados["obras"]:
        dia, mes, ano = map(int, o["data"].split("/"))
        obra = Obra(
            o["id"],
            o["descricao"],
            Data(dia, mes, ano),
            empreiteiro=empreiteiros[o["empreiteiro"]]
        )
        for nome_eq in o["equipamentos"]:
            obra.inserir_equipamento(equipamentos[nome_eq])
        inserir_obra(obra)

    for c in dados["contratos"]:
        dia, mes, ano = map(int, c["data"].split("/"))
        criar_contrato(
            c["obra_id"],
            c["empreiteiro"],
            c["equipamento"],
            c["valor"],
            Data(dia, mes, ano),
            c["prazo"]
        )


if __name__ == '__main__':
    print('\nAlocação de Equipamentos da Construção Civil')

    caminho_entrada = os.path.join(os.path.dirname(__file__), "..", "..", "dados", "arquivo_entrada.json")
    caminho_entrada = os.path.normpath(caminho_entrada)

    carregar_objetos_arquivo(caminho_entrada)

    caminho_saida = os.path.join(os.path.dirname(__file__), "..", "..", "dados", "arquivo_saida.txt")
    caminho_saida = os.path.normpath(caminho_saida)

    run_interface(caminho_saida)
