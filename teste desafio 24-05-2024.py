# -- produtos = {
# --     "Arroz": ["Alimento", "Grão", 10.0, 1, 50],
# --     "Feijão": ["Alimento", "Grão", 8.0, 2, 20],
# --     "Macarrão": ["Alimento", "Massas", 5.0, 3, 30],
# --     "Pasta de Dente": ["Higiene", "Higiene", 2.0, 4, 100],
# --     "Batata": ["Alimento", "Verduras", 6.0, 5, 80]
# -- }

# -- carrinho = {}

# -- nome_cliente = input("Digite seu nome: ")

# -- escolha = int(input(f"\nOlá Cliente {nome_cliente}, Bem Vindo ao Sistema do Mercado!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para Consultar um produto\nDigite 2 - para adicionar produto ao Carrinho\nDigite 3 - para excluir produto do Carrinho\nDigite 4 - para Visualizar o carrinho\nDigite 5 - para Fechar o carrinho\nDigite 9 - para Sair\nDigite aqui:> "))

# -- while escolha != 9:
# --     if escolha == 1:
# --         busca = input("Digite o nome do produto que você quer buscar: ")
# --         if busca in produtos:
# --             print(f"Produto: {busca}\nDescrição: {produtos[busca][0]}\nSubtipo: {produtos[busca][1]}\nPreço: R${produtos[busca][2]}\nCodigo: {produtos[busca][3]}\nQuantidade atual do estoque: {produtos[busca][4]}")
# --         else:
# --             print("Produto não encontrado.")
# --     elif escolha == 2:
# --         escolha_produto = input("Digite o nome do produto que você quer adicionar ao carrinho: ")
# --         if escolha_produto in produtos:
# --             quantidade = int(input(f"Digite a quantidade de {escolha_produto} que você quer adicionar ao carrinho: "))
# --             if produtos[escolha_produto][4] >= quantidade:
# --                 if escolha_produto in carrinho:
# --                     carrinho[escolha_produto] += quantidade
# --                 else:
# --                     carrinho[escolha_produto] = quantidade
# --                 produtos[escolha_produto][4] -= quantidade
# --                 print(f"{quantidade} unidades de {escolha_produto} foram adicionadas ao carrinho.")
# --             else:
# --                 print(f"Desculpe, não há quantidade suficiente de {escolha_produto} no estoque.")
# --         else:
# --             print("Produto não encontrado.")
# --     elif escolha == 3:
# --         escolha_produto = input("Digite o nome do produto que você quer remover do carrinho: ")
# --         if escolha_produto in carrinho:
# --             quantidade = int(input(f"Digite a quantidade de {escolha_produto} que você quer remover do carrinho: "))
# --             if carrinho[escolha_produto] >= quantidade:
# --                 carrinho[escolha_produto] -= quantidade
# --                 produtos[escolha_produto][4] += quantidade
# --                 if carrinho[escolha_produto] == 0:
# --                     del carrinho[escolha_produto]
# --                 print(f"{quantidade} unidades de {escolha_produto} foram removidas do carrinho.")
# --             else:
# --                 print(f"Você não tem essa quantidade de {escolha_produto} no carrinho.")
# --         else:
# --             print("Produto não encontrado no carrinho.")
# --     elif escolha == 4:
# --         print("\nItens no carrinho:")
# --         total = 0
# --         for item, qtd in carrinho.items():
# --             preco = produtos[item][2]
# --             subtotal = preco * qtd
# --             total += subtotal
# --             print(f"{item}: {qtd} unidades, R${preco} cada, Subtotal: R${subtotal:.2f}")
# --         print(f"Total a pagar: R${total:.2f}")
# --     elif escolha == 5:
# --         print("\nItens no carrinho:")
# --         total = 0
# --         for item, qtd in carrinho.items():
# --             preco = produtos[item][2]
# --             subtotal = preco * qtd
# --             total += subtotal
# --             print(f"{item}: {qtd} unidades, R${preco} cada, Subtotal: R${subtotal:.2f}")
# --         print(f"Total a pagar: R${total:.2f}")

# --         imposto_municipal = 0.12
# --         imposto_estadual = 0.08
# --         imposto_nacional = 0.05
# --         total_com_imposto_municipal = total * imposto_municipal
# --         total_com_imposto_estadual = total * imposto_estadual
# --         total_com_imposto_nacional = total * imposto_nacional
# --         total_nota_fiscal = total + total_com_imposto_municipal + total_com_imposto_estadual + total_com_imposto_nacional

# --         print(f"Total de impostos: Municipal: R${total_com_imposto_municipal:.2f}, Estadual: R${total_com_imposto_estadual:.2f}, Nacional: R${total_com_imposto_nacional:.2f}")
# --         print(f"Total com impostos: R${total_nota_fiscal:.2f}")

# --         pagamento = int(input("\nEscolha agora a forma de pagamento!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para pagar no Dinheiro\nDigite 2 - para Pagar com PIX\nDigite 3 - para pagar com Cartão de Cred/Deb/Voucher\nDigite aqui:> "))
        
# --         if pagamento == 1:
# --             pagamento_cliente = float(input("Qual valor pago pelo cliente? "))
# --             if pagamento_cliente >= total_nota_fiscal:
# --                 troco = pagamento_cliente - total_nota_fiscal
# --                 print(f"O troco a ser devolvido é: R${troco:.2f}")
# --                 print("Obrigado por comprar conosco!")
# --                 carrinho.clear()
# --             else:
# --                 print(f"Compra não autorizada, valor pago R${pagamento_cliente:.2f} é menor que o valor total da compra! R${total_nota_fiscal:.2f}")
# --                 print("Escolha outra forma de pagamento!")
# --         elif pagamento == 2:
# --             pagamento_cliente = float(input("Qual o saldo existente? "))
# --             if pagamento_cliente >= total_nota_fiscal:
# --                 print("Compra aprovada!!!")
# --                 print("Obrigado por comprar conosco!")
# --                 carrinho.clear()
# --             else:
# --                 print(f"Compra não autorizada, saldo R${pagamento_cliente:.2f} é menor que o valor total da compra! R${total_nota_fiscal:.2f}")
# --                 print("Escolha outra forma de pagamento!")
# --         elif pagamento == 3:
# --             pagamento_cliente = float(input("Qual o saldo existente? "))
# --             if pagamento_cliente >= total_nota_fiscal:
# --                 print("Compra aprovada!!!")
# --                 print("Obrigado por comprar conosco!")
# --                 carrinho.clear()
# --             else:
# --                 print(f"Compra não autorizada, saldo R${pagamento_cliente:.2f} é menor que o valor total da compra! R${total_nota_fiscal:.2f}")
# --                 print("Escolha outra forma de pagamento!")
# --         else:
# --             print("Opção inválida.")
# --     else:
# --         print("Opção inválida.")
    
# --     escolha = int(input("\nDigite 1 para Consultar um produto\nDigite 2 para adicionar produto ao Carrinho\nDigite 3 - para excluir produto do Carrinho\nDigite 4 - para Visualizar o carrinho\nDigite 5 - para Fechar o carrinho\nDigite 9 - para Sair\nDigite aqui:> "))

# -- print("Saindo do programa...")
# Definição dos produtos por seção
produtos_por_secao = {
    "Alimentos": {
        "Grãos": {
            "Arroz": {"Preço": 10.0, "Quantidade": 50},
            "Feijão": {"Preço": 8.0, "Quantidade": 20},
        },
        "Massas": {
            "Macarrão": {"Preço": 5.0, "Quantidade": 30},
        },
        "Verduras": {
            "Batata": {"Preço": 6.0, "Quantidade": 80},
        }
    },
    "Higiene": {
        "Higiene": {
            "Pasta de Dente": {"Preço": 2.0, "Quantidade": 100},
        }
    }
}

carrinho = []

# Função para mostrar as seções disponíveis
def mostrar_secoes():
    print("\nSeções Disponíveis:")
    for secao in produtos_por_secao:
        print(secao)

# Função para mostrar os subtipos disponíveis em uma seção
def mostrar_subtipos(secao):
    print(f"\nSubtipos disponíveis em {secao}:")
    for subtipo in produtos_por_secao[secao]:
        print(subtipo)

# Função para mostrar os produtos disponíveis em uma seção e subtipo
def mostrar_produtos(secao, subtipo=None):
    if subtipo:
        print(f"\nProdutos disponíveis em {subtipo} ({secao}):")
        for produto in produtos_por_secao[secao][subtipo]:
            print(produto)
    else:
        print(f"\nProdutos disponíveis em {secao}:")
        for subtipo in produtos_por_secao[secao]:
            for produto in produtos_por_secao[secao][subtipo]:
                print(produto)

# Função para adicionar um produto ao carrinho
def adicionar_produto(secao, subtipo=None, produto=None):
    if subtipo and produto:
        if produto in produtos_por_secao[secao][subtipo]:
            carrinho.append((produto, produtos_por_secao[secao][subtipo][produto]["Preço"]))
            print(f"\n{produto} adicionado ao carrinho.")
            produtos_por_secao[secao][subtipo][produto]["Quantidade"] -= 1
        else:
            print("Produto não encontrado.")
    elif subtipo:
        print("Por favor, escolha um produto válido.")
    elif secao:
        print("Por favor, escolha um subtipo e um produto.")

# Função para remover um produto do carrinho
def remover_produto(produto):
    if produto in [item[0] for item in carrinho]:
        carrinho.remove((produto, [item[1] for item in carrinho if item[0] == produto][0]))
        print(f"\n{produto} removido do carrinho.")
    else:
        print("Produto não encontrado no carrinho.")

# Função para finalizar a compra e exibir o valor total
def finalizar_compra():
    total = sum(item[1] for item in carrinho)
    print("\nProdutos no Carrinho:")
    for item in carrinho:
        print(f"{item[0]}: R${item[1]:.2f}")
    print(f"\nTotal a pagar: R${total:.2f}")
    carrinho.clear()

# Loop principal do programa
print("Bem-vindo ao Supermercado!\n")
mostrar_secoes()

while True:
    secao = input("\nEscolha uma seção ou digite 'Sair' para finalizar: ").capitalize()
    if secao == 'Sair':
        print("\nSaindo do programa...")
        break
    elif secao in produtos_por_secao:
        mostrar_subtipos(secao)
        subtipo = input("\nEscolha um subtipo ou digite 'Voltar' para escolher outra seção: ").capitalize()
        if subtipo == 'Voltar':
            continue
        elif subtipo in produtos_por_secao[secao]:
            mostrar_produtos(secao, subtipo)
            produto = input("\nEscolha um produto ou digite 'Voltar' para escolher outro subtipo: ").capitalize()
            if produto == 'Voltar':
                continue
            else:
                adicionar_produto(secao, subtipo, produto)
        else:
            print("Subtipo inválido.")
    else:
        print("Seção inválida.")

    continuar = input("\nDeseja continuar comprando? (S/N): ").upper()
    if continuar != 'S':
        break

# Finaliza a compra se houver itens no carrinho
if carrinho:
    finalizar_compra()