produtos = [["Arroz", "Alimento", "Grão", 10.0, 1, 50],["Feijão", "Alimento", "Grão", 8.0, 2, 20],["Macarrão", "Alimento", "Massas", 5.0, 3, 30],["Pasta de Dente", "Higiene", "Higiene", 2.0, 4, 100],["Batata", "Alimento", "Verduras", 6.0, 5, 80]]
carrinho = []
login = int(input("\nOlá, Bem Vindo ao Sistema do Mercado!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para sistemas de clientes\nDigite 2 - para sistemas de funcionários\nEscolha aqui>>>"))
if login == 1:
    cpf_cliente = int(input("Digite seu CPF: "))
    nome_cliente = input("Digite seu Nome:")
    escolha = int(input(f"\nOlá Cliente {nome_cliente}, Bem Vindo ao Sistema do Mercado!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para Consultar um produto\nDigite 2 - para adicionar produto ao Carrinho\nDigite 3 - para excluir produto do Carrinho\nDigite 4 - para Visualizar o carrinho\nDigite 5 - para Fechar o carrinho\nDigite 9 - para Sair\nDigite aqui:> "))  # menuzinho
    while escolha != 9:
        if escolha == 1:
            busca = input("Digite o nome do produto que você quer buscar: ")
            found = False
            for produto in produtos:
                if produto[0] == busca:
                    print(f"Produto: {produto[0]}\nDescrição: {produto[1]}\nSubtipo: {produto[2]}\nPreço: R${produto[3]}\nCódigo: {produto[4]}\nQuantidade atual do estoque: {produto[5]}")
                    found = True
                    break
            if not found:
                print("Produto não encontrado.")
        elif escolha == 2:
            print("Os produtos disponíveis atualmente são:")
            for produto in produtos:
                print(f"Nome: {produto[0]}, Seção: {produto[1]}, Subtipo: {produto[2]}, Preço: R${produto[3]}, Quantidade: {produto[5]} Uni.")
#################################################################################lista para escolher produto####################################################################################################
            escolha_produto = input("Digite o nome do produto que você quer adicionar ao carrinho: ")
            found = False
            for produto in produtos:
                if produto[0] == escolha_produto:
                    quantidade = int(input(f"Digite a quantidade de {escolha_produto} que você quer adicionar ao carrinho: "))
                    if produto[5] >= quantidade:
                        carrinho.append([produto[0], quantidade, produto[3]])
                        produto[5] -= quantidade
                        print(f"{quantidade} unidades de {escolha_produto} foram adicionadas ao carrinho.")
                    else:
                        print(f"Desculpe, não há quantidade suficiente de {escolha_produto} no estoque.")
                    found = True
                    break
            if not found:
                print("Produto não encontrado.")
        elif escolha == 3:
            escolha_produto = input("Digite o nome do produto que você quer remover do carrinho: ")
            found = False
            for item in carrinho:
                if item[0] == escolha_produto:
                    quantidade = int(input(f"Digite a quantidade de {escolha_produto} que você quer remover do carrinho: "))
                    if item[1] >= quantidade:
                        item[1] -= quantidade
                        found = True
                        break
                    else:
                        print(f"Você não tem essa quantidade de {escolha_produto} no carrinho.")
                        found = True
                        break
            if not found:
                print("Produto não encontrado no carrinho.")
        elif escolha == 4:
            print("\nItens no carrinho:")
            total = 0
            for item in carrinho:
                subtotal = item[1] * item[2]
                total += subtotal
                print(f"{item[0]}: {item[1]} unidades, R${item[2]} cada, Subtotal: R${subtotal:.2f}")
            print(f"Total a pagar: R${total:.2f}")
        elif escolha == 5:
            print("\nItens no carrinho:")
            total = 0
            for item in carrinho:
                subtotal = item[1] * item[2]
                total += subtotal
                print(f"{item[0]}: {item[1]} unidades, R${item[2]} cada, Subtotal: R${subtotal:.2f}")
            print(f"Total a pagar: R${total:.2f}")
            imposto_municipal = 0.12
            imposto_estadual = 0.08
            imposto_nacional = 0.05
            total_com_imposto_municipal = total * imposto_municipal
            total_com_imposto_estadual = total * imposto_estadual
            total_com_imposto_nacional = total * imposto_nacional
            total_nota_fiscal = total + total_com_imposto_municipal + total_com_imposto_estadual + total_com_imposto_nacional
            print(f"Total de impostos: Municipal: R${total_com_imposto_municipal:.2f}, Estadual: R${total_com_imposto_estadual:.2f}, Nacional: R${total_com_imposto_nacional:.2f}")
            print(f"Total com impostos: R${total_nota_fiscal:.2f}")
            pagamento = int(input("\nEscolha agora a forma de pagamento!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para pagar no Dinheiro\nDigite 2 - para Pagar com PIX\nDigite 3 - para pagar com Cartão de Crédito/Débito/Voucher\nDigite aqui:> "))
            if pagamento == 1:
                pagamento_cliente = float(input("Qual valor pago pelo cliente? "))
                if pagamento_cliente >= total_nota_fiscal:
                    troco = pagamento_cliente - total_nota_fiscal
                    print(f"O troco a ser devolvido é: R${troco:.2f}")
                    print("Obrigado por comprar conosco!")
                    carrinho.clear()
                else:
                    print(f"Compra não autorizada, valor pago R${pagamento_cliente:.2f} é menor que o valor total da compra! R${total_nota_fiscal:.2f}")
                    print("Escolha outra forma de pagamento!")
            elif pagamento == 2 or pagamento == 3:
                print("Compra aprovada!!!")
                print("Obrigado por comprar conosco!")
                carrinho.clear()
            else:
                print("Opção inválida.")
        else:
            print("Opção inválida.")
        escolha = int(input("\nDigite 1 para Consultar um produto\nDigite 2 para adicionar produto ao Carrinho\nDigite 3 - para excluir produto do Carrinho\nDigite 4 - para Visualizar o carrinho\nDigite 5 - para Fechar o carrinho\nDigite 9 - para Sair\nDigite aqui:> "))
    print("Saindo do programa...")
############################################################################### PERFIL FUNCIONARIO ###############################################################################
elif login == 2:
    matricula = input("Digite sua matricula: ")
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    cpf = int(input("Digite seu CPF: "))
    escolha = int(input(f"\nOlá Funcionario {nome}, Bem Vindo ao Sistema do Mercado!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para Consultar o estoque\nDigite 2 - para Adicionar unidades a um Produto\nDigite 3 - para Excluir unidades de um produto\nDigite 4 - para Cadastrar um novo produto\nDigite 5 - para Alterar o preço de um produto\nDigite 9 - para Sair\nDigite aqui:> "))  # menuzinho
    while escolha != 9:
        if escolha == 1:
            busca = input("Digite o nome do produto que você quer buscar: ")
            found = False
            for produto in produtos:
                if produto[0] == busca:
                    print(f"Produto: {produto[0]}\nDescrição: {produto[1]}\nSubtipo: {produto[2]}\nPreço: R${produto[3]}\nCódigo: {produto[4]}\nQuantidade atual do estoque: {produto[5]}")
                    found = True
                    break
            if not found:
                print("Produto não encontrado.")
        elif escolha == 2:
            adicionar = input("Digite o nome do produto para adicionar itens: ")
            found = False
            for produto in produtos:
                if produto[0] == adicionar:
                    print(f"Produto: {adicionar}\nDescrição: {produto[1]}\nQuantidade atual no estoque: {produto[5]}")
                    print(f"Quantos itens você quer incluir em {adicionar}?")
                    adc = int(input("Digite a quantidade: "))
                    soma = produto[5]
                    result = soma + adc
                    produto[5] = result
                    print(f"Foram adicionadas {adc} unidades no produto {adicionar}, O estoque atualizado é: {produto[5]}")
                    found = True
                    break
            if not found:
                print("Produto não encontrado.")
        elif escolha == 3:
            remover = input("Digite o nome do produto para remover itens: ")
            found = False
            for produto in produtos:
                if produto[0] == remover:
                    print(f"Produto: {remover}\nDescrição: {produto[1]}\nQuantidade atual no estoque: {produto[5]}")
                    print(f"Quantos itens você quer remover em {remover}?")
                    rem = int(input("Digite a quantidade: "))
                    subtracao = produto[5]
                    result = subtracao - rem
                    produto[5] = result
                    print(f"Foram removidas {rem} unidades no produto {remover}, O estoque atualizado é: {produto[5]}")
                    found = True
                    break
            if not found:
                print("Produto não encontrado.")
        elif escolha == 4:
            nome_novo = input("Digite o nome do novo produto: ")
            desc_novo = input("Digite a descrição do novo produto: ")
            tipo_novo = input("Digite o tipo do novo produto: ")
            preco_novo = float(input("Digite o preço do novo produto: "))
            cod_novo = int(input("Digite o código do novo produto: "))
            quant_novo = int(input("Digite a quantidade do novo produto: "))
            produtos.append([nome_novo, desc_novo, tipo_novo, preco_novo, cod_novo, quant_novo])
            print(f"Novo produto {nome_novo} adicionado com sucesso!")
        elif escolha == 5:
            atu_preco = input("Digite o nome do produto para atualizar o preço: ")
            found = False
            for produto in produtos:
                if produto[0] == atu_preco:
                    print(f"Produto: {atu_preco}\nDescrição: {produto[1]}\nPreço Atual: {produto[3]}")
                    preco_new = float(input("Digite o novo preço do novo produto: "))
                    produto[3] = preco_new
                    print(f"O preço do produto {atu_preco} foi atualizado, O preço atual é: {produto[3]}")
                    found = True
                    break
            if not found:
                print("Produto não encontrado.")
        else:
            print("Opção inválida.")
        escolhab = int(input("Digite 9 para finalizar ou 0 para voltar ao MENU: "))
        if escolhab == 9:
            break
        elif escolhab == 0:
            escolha = int(input("\nOlá Funcionario, Bem Vindo ao Sistema do Mercado!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para Consultar o estoque\nDigite 2 - para Adicionar unidades a um Produto\nDigite 3 - para Excluir unidades de um produto\nDigite 4 - para Cadastrar um novo produto\nDigite 5 - para Alterar o preço de um produto\nDigite 9 - para Sair\nDigite aqui:> "))  # menuzinho
        else:
            print("Digite uma das opções válidas: 9 para finalizar ou 0 para voltar ao menu!")
    print("Saindo do programa...")





