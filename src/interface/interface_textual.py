import json
import os
from src.util.gerais import imprimir_objetos, ordenar_objetos_por_um_atributo, ordenar_objetos_por_dois_atributos
from src.entidades.empreiteiro import get_empreiteiros
from src.entidades.equipamento import get_equipamentos
from src.entidades.obra import get_obras
from src.entidades.contrato import get_contratos

def salvar_objetos_arquivo(caminho_arquivo):
    dados = {}

    dados["empreiteiros"] = [
        {
            "nome": e.nome,
            "telefone": e.telefone,
            "email": e.email,
            "endereço": e.endereço
        }
        for e in get_empreiteiros().values()
    ]

    dados["equipamentos"] = [
        {
            "nome": eq.nome,
            "tipo": eq.tipo,
            "valor": eq.valor,
            "peso": eq.peso,
            "disponivel": eq.disponivel
        }
        for eq in get_equipamentos().values()
    ]

    dados["obras"] = []
    for o in get_obras().values():
        dados["obras"].append({
            "id": o.id,
            "descricao": o.descricao,
            "data_inicio": str(o.data_inicio),
            "empreiteiro": o.empreiteiro.nome if o.empreiteiro else "",
            "equipamentos": [eq.nome for eq in o.listar_equipamentos()]
        })

    dados["contratos"] = []
    for c in get_contratos():
        dados["contratos"].append({
            "obra_id": c.obra.id,
            "empreiteiro": c.empreiteiro.nome,
            "valor": c.valor,
            "data": str(c.data_assinatura),
            "prazo": c.prazo
        })

    with open(caminho_arquivo, mode="w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print(f"\nDados gravados com sucesso em: {caminho_arquivo}")


def run_interface(caminho_saida):
    opcao = ""
    while opcao != "0":
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Listar Empreiteiros")
        print("2 - Listar Obras")
        print("3 - Listar Equipamentos")
        print("4 - Listar Contratos")
        print("5 - Listar Equipamentos por Obra")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").upper()

        if opcao == "1":
            imprimir_objetos('Empreiteiro : nome, telefone, email, endereço', get_empreiteiros().values())

        elif opcao == "2":
            imprimir_objetos('Obra : id, descrição, data, empreiteiro', get_obras().values())

        elif opcao == "3":
            imprimir_objetos('Equipamento: nome, tipo, valor, peso, status', get_equipamentos().values())

        elif opcao == "4":
            imprimir_objetos('Contrato : obra, empreiteiro, equipamento, valor, data, prazo', get_contratos())

        elif opcao == "5":
            obras = list(get_obras().values())
            print("\nObras disponíveis:\n")
            for i, obra in enumerate(obras, start=1):
                print(f"{i} - {obra.descricao}")

            try:
                escolha = int(input("\nDigite o número da obra para listar os equipamentos: "))
                if 1 <= escolha <= len(obras):
                    obra = obras[escolha - 1]
                    print(f"\n=== {obra.descricao} ===")

                    equipamentos_obra = obra.listar_equipamentos()
                    if not equipamentos_obra:
                        print("Nenhum equipamento alocado para esta obra.")
                    else:
                        imprimir_objetos('Equipamento : nome, tipo, valor, peso, status', equipamentos_obra)

                        equipamentos_ordenados = ordenar_objetos_por_um_atributo(
                            objetos=equipamentos_obra,
                            atributo=lambda e: e.valor,
                            ordenação_decrescente=True
                        )
                        imprimir_objetos('Equipamentos ordenados por valor (decrescente)', equipamentos_ordenados)

                        equipamentos_ordenados = ordenar_objetos_por_um_atributo(
                            objetos=equipamentos_obra,
                            atributo=lambda e: e.peso,
                            ordenação_decrescente=False
                        )
                        imprimir_objetos('Equipamentos ordenados por peso (crescente)', equipamentos_ordenados)

                        equipamentos_ordenados = ordenar_objetos_por_dois_atributos(
                            objetos=equipamentos_obra,
                            atributo1=lambda e: e.valor,
                            atributo2=lambda e: e.peso,
                            ordenação_decrescente=True
                        )
                        imprimir_objetos('Equipamentos ordenados por valor e peso (decrescente)', equipamentos_ordenados)
                else:
                    print("\nOpção inválida. Nenhuma obra selecionada.")
            except ValueError:
                print("\nEntrada inválida. Digite um número correspondente à obra.")

        elif opcao == "0":
            print("\nSaindo do sistema...")

        else:

            print("\nOpção inválida, tente novamente.")

        from src.interface.interface_textual import salvar_objetos_arquivo
        salvar_objetos_arquivo(caminho_saida)
