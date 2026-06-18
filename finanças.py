from datetime import datetime



# categorias
# salario, luz, agua, etc...


def cadastrar_categoria():
    categoria = input("Digite o nome da categoria: ")

    with open("categorias.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(categoria + "\n")

    print("Categoria cadastrada com sucesso!")


def listar_categorias():
    try:
        with open("categorias.txt", "r", encoding="utf-8") as arquivo:
            categorias = arquivo.readlines()

        if len(categorias) == 0:
            print("Nenhuma categoria cadastrada.")
            return []

        print("\n===== CATEGORIAS =====")

        lista = []

        for i, categoria in enumerate(categorias, start=1):
            categoria = categoria.strip()
            lista.append(categoria)
            print(f"{i} - {categoria}")

        return lista

    except FileNotFoundError:
        print("Nenhuma categoria cadastrada.")
        return []



# entrada e saida (entrada +money, saida -money)



def registrar_entrada():
    categorias = listar_categorias()

    if len(categorias) == 0:
        print("Cadastre uma categoria primeiro.")
        return

    try:
        opcao = int(input("Escolha a categoria da entrada: "))

        if opcao < 1 or opcao > len(categorias):
            print("Categoria inválida.")
            return

        categoria = categorias[opcao - 1]

        valor = float(input("Valor da entrada: R$ "))

        data = datetime.now().strftime("%d/%m/%Y")

        with open("movimentacoes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"entrada;{valor};{categoria};{data}\n"
            )

        print("Entrada registrada com sucesso!")

    except ValueError:
        print("Valor inválido!")



def registrar_saida():
    categorias = listar_categorias()

    if len(categorias) == 0:
        return

    try:
        opcao = int(input("Escolha o número da categoria: "))

        if opcao < 1 or opcao > len(categorias):
            print("Categoria inválida.")
            return

        categoria = categorias[opcao - 1]

        valor = float(input("Valor da saída: R$ "))

        data = datetime.now().strftime("%d/%m/%Y")

        with open("movimentacoes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"saida;{valor};{categoria};{data}\n")

        print("Saída registrada com sucesso!")

    except ValueError:
        print("Valor inválido!")



# relatorio (soma das entrada, saida e o resultado do saldo)



def relatorio():
    entradas = 0
    saidas = 0

    try:
        with open("movimentacoes.txt", "r", encoding="utf-8") as arquivo:

            for linha in arquivo:
                dados = linha.strip().split(";")

                if dados[0] == "entrada":
                    entradas += float(dados[1])

                elif dados[0] == "saida":
                    saidas += float(dados[1])

        saldo = entradas - saidas

        relatorio_texto = (
            "===== RELATÓRIO FINANCEIRO =====\n"
            f"Total de Entradas: R$ {entradas:.2f}\n"
            f"Total de Saídas: R$ {saidas:.2f}\n"
            f"Saldo Atual: R$ {saldo:.2f}\n"
        )

        print("\n" + relatorio_texto)

        with open(
            "relatorio_financeiro.txt",
            "w",
            encoding="utf-8"
        ) as arquivo:
            arquivo.write(relatorio_texto)

        print("Relatório salvo em relatorio_financeiro.txt")

    except FileNotFoundError:
        print("Nenhuma movimentação encontrada.")



# movimentações


def listar_movimentacoes():
    try:
        with open("movimentacoes.txt", "r", encoding="utf-8") as arquivo:

            print("\n===== MOVIMENTAÇÕES =====")

            for linha in arquivo:
                dados = linha.strip().split(";")

                print(
                    f"Tipo: {dados[0].upper()} | "
                    f"Valor: R$ {float(dados[1]):.2f} | "
                    f"Categoria: {dados[2]} | "
                    f"Data: {dados[3]}"
                )

    except FileNotFoundError:
        print("Nenhuma movimentação cadastrada.")



# menu gigante ta doido



def menu():
    while True:

        print("\n==============================")
        print(" SISTEMA DE FINANÇAS PESSOAIS ")
        print("==============================")
        print("1 - Cadastrar categoria")
        print("2 - Listar categorias")
        print("3 - Registrar entrada")
        print("4 - Registrar saída")
        print("5 - Listar movimentações")
        print("6 - Relatório financeiro")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_categoria()

        elif opcao == "2":
            listar_categorias()

        elif opcao == "3":
            registrar_entrada()

        elif opcao == "4":
            registrar_saida()

        elif opcao == "5":
            listar_movimentacoes()

        elif opcao == "6":
            relatorio()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


menu()
