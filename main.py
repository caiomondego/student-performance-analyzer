import json

ARQUIVO = "data.json"


def carregar_dados():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []


def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)


def adicionar_aluno(dados):
    nome = input("Nome do aluno: ")
    dados.append({"nome": nome, "notas": []})
    salvar_dados(dados)


def adicionar_nota(dados):
    nome = input("Nome do aluno: ")

    for aluno in dados:
        if aluno["nome"] == nome:
            nota = float(input("Nota: "))
            aluno["notas"].append(nota)
            salvar_dados(dados)
            print("Nota adicionada!")
            return

    print("Aluno não encontrado!")


def listar_alunos(dados):
    for aluno in dados:
        if len(aluno["notas"]) > 0:
            media = sum(aluno["notas"]) / len(aluno["notas"])
            status = "Aprovado" if media >= 6 else "Reprovado"
            print(f'{aluno["nome"]} - média {media:.2f} ({status})')
        else:
            print(f'{aluno["nome"]} - sem notas')


def main():
    dados = carregar_dados()

    while True:
        print("\n1 - Adicionar aluno")
        print("2 - Adicionar nota")
        print("3 - Listar alunos")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_aluno(dados)
        elif opcao == "2":
            adicionar_nota(dados)
        elif opcao == "3":
            listar_alunos(dados)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


main()