# Função para adicionar um contato
def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ").strip()
    telefone = input("Digite o telefone do contato: ").strip()
    
    if nome in agenda:
        print(f"O contato {nome} já existe. Deseja atualizar o número? (s/n)")
        opcao = input().strip().lower()
        if opcao == 's':
            agenda[nome] = telefone
            print(f"Contato {nome} atualizado com sucesso.")
        else:
            print("Operação cancelada.")
    else:
        agenda[nome] = telefone
        print(f"Contato {nome} adicionado com sucesso.")

# Função para buscar um contato
def buscar_contato(agenda):
    nome = input("Digite o nome do contato que deseja buscar: ").strip()
    if nome in agenda:
        print(f"Telefone de {nome}: {agenda[nome]}")
    else:
        print(f"Contato {nome} não encontrado.")

# Função para remover um contato
def remover_contato(agenda):
    nome = input("Digite o nome do contato que deseja remover: ").strip()
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} removido com sucesso.")
    else:
        print(f"Contato {nome} não encontrado.")

# Função principal para exibir o menu e processar as escolhas do usuário
def menu():
    agenda = {}
    while True:
        print("\nAgenda Telefônica")
        print("1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Remover contato")
        print("4. Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            adicionar_contato(agenda)
        elif escolha == '2':
            buscar_contato(agenda)
        elif escolha == '3':
            remover_contato(agenda)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
