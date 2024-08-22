from datetime import datetime

produtos = {}

def cadastrar_produto():
    nome = input("Digite o nome do produto:\n")
    codigo = input("Digite o código do produto:\n")
    quantidade = int(input("Digite a quantidade do produto:\n"))

    if codigo in produtos:
        print("Código do produto já existe. Tente novamente.")
        return

    produtos[codigo] = {
        "nome": nome,
        "quantidade": quantidade,
        "data de entrada": datetime.now(),
        "status": "sem defeito"
    }
    print(f"Produto {nome} cadastrado com sucesso.")

def consultar_estoque():
    if not produtos:
        print("O estoque está vazio.")
        return

    print("\nLista de produtos em estoque:")
    for codigo, produto in produtos.items():
        print("Código:", codigo)
        print("Nome:", produto['nome'])
        print("Quantidade:", produto['quantidade'])
        print(f"Data de entrada: {produto['data de entrada'].strftime('%d/%m/%Y')}")
        print("Status:", produto['status'])

def validar_produto():
    codigo = input("Digite o código do produto: ")

    if codigo not in produtos:
        print("O código do produto não existe.")
        return

    produto = produtos[codigo]
    status = input(f"O produto {produto['nome']} está com defeito? (sim/não): ")
    if status.lower() == "sim":
        produto["status"] = "com defeito"
        print(f"Produto {produto['nome']} marcado com defeito.")
        print("Fornecedor contactado com sucesso.")
    else:
        print(f"Produto {produto['nome']} validado como sem defeito.")

def menu_principal():
    print("\nMenu Principal")
    print("1. Cadastrar produto")
    print("2. Consultar Estoque")
    print("3. Validar produto")
    print("4. Sair")

    opcao = input("Digite uma das opções:\n")
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        consultar_estoque()
    elif opcao == "3":
        validar_produto()
    elif opcao == "4":
        print("Saindo do sistema...")
        exit()
    else:
        print("Opção inválida.")

while True:
    menu_principal()