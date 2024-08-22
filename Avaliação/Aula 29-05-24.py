# 1. Contagem de Palavras:
# ○ Crie um programa que leia um texto e conte quantas vezes cada palavra aparece.
# Armazene as palavras e suas contagens em um dicionário.

# texto = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# textoCortado = texto.upper().split("")
# for i in textoCortado:
#     x = textoCortado.count(i)
#     dicionario.update({i:x})
# print(dicionario)


# texto = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# dicionario = {}
# for i in texto:
#     if i in dicionario:
#         dicionario[i] += 1
#     else:
#         dicionario[i] = 1
# print(dicionario)

########################################################################################################################################################################################################################################################################
#2. Média de Notas:
# ○ Crie um dicionário com nomes de alunos e suas notas. Calcule a média das
# notas e exiba o resultado.

# dicionario = {"Roger" : [1,2,3], "Lucas" : [0,0,0], "Jessica" : [6,7,8]}
# for x,i in dicionario.items():
#     y = sum (i)/3
#     print ("Aluno: ", x , "Media" , y)
########################################################################################################################################################################################################################################################################
#3. Agenda Telefônica:
# ○ Crie um programa que permita adicionar, buscar e remover contatos de uma
# agenda telefônica usando um dicionário.

# Função para adicionar um contato
# agenda = {}
# while True:
#     print("\nAgenda Telefônica!!!!!")
#     print("1 - Adicionar contato")
#     print("2 - Buscar contato")
#     print("3 - Remover contato")
#     print("4 - Sair")
#     escolha = int(input("Digite a opção desejada> "))

#     if escolha == 1:
#         nome = input("Digite o nome do contato: ")
#         telefone = input("Digite o telefone do contato: ")
#         if nome in agenda:
#             print(f"O contato {nome} já existe com o número {agenda[nome]}.")
#             opcao = input("Deseja atualizar o número? (s/n): ")
#             if opcao == 's':
#                 agenda[nome] = telefone
#                 print(f"Contato {nome} atualizado com sucesso.")
#             else:
#                 print("Operação cancelada.")
#         else:
#             agenda[nome] = telefone
#             print(f"\nContato {nome} adicionado com sucesso.")
#     elif escolha == 2:
#         nome_busc = input("Digite o nome do contato para buscar: ")
#         if nome_busc in agenda:
#             print("\nDados do contato buscado:")
#             print(f"Telefone de {nome_busc}: {agenda[nome_busc]}")
#         else:
#             print("Contato não encontrado!!!")
#     elif escolha == 3:
#         nome_rem = input("Digite o nome do contato para remover: ")
#         if nome_rem in agenda:
#             del agenda[nome_rem]
#             print(f"Contato {nome_rem} removido com sucesso.")
#         else:
#             print("Contato não encontrado!!!")
#     elif escolha == 4:
#         print("SAINDO.....")
#         break
#     else:
#         print("Opção Inválida!!!")
########################################################################################################################################################################################################################################################################
#4. Tradutor Simples:
# ○ Crie um dicionário com algumas palavras em inglês e suas traduções em
# português. Peça ao usuário para digitar uma palavra em inglês e exiba a tradução
# agenda = {"Dog" : "Cachorro" , "Cat" : "Gato" , "Bird" : "Passaro" , "Rabbit" : "Coelho" , "Tortoise" : "Tartaruga" , }
# tradu = input("Digite a palavra para traduzir: ")
# if tradu in agenda:
#     print(f"A tradução para o termo buscado é: {agenda[tradu]}")
# print("Saindo....")
########################################################################################################################################################################################################################################################################
#5.Controle de Estoque:
# ○ Crie um dicionário para controlar o estoque de produtos em uma loja. Permita
# adicionar, remover e atualizar a quantidade de cada produto.
# produtos = {"Arroz":["Alimento","Grão", 10.0 , 1,  50] , "Feijão":["Alimento","Grão", 8.0 , 2, 20 ], "Macarrão":["Alimento","Massas", 5.0 , 3 , 30], "Pasta de Dente":["Higiene","Higiene", 2.0 , 4, 100], "Batata":["Alimento","Verduras", 6.0 , 5 , 80]}
#             #Nome       Class    Tipo  preço  cod quant
# carrinho = {}
# tirar_repetidos = []
# #for chave in produtos:
# #    print(f"O produto é {chave}, Descrição: {produtos[chave][0]}, Subtipo: {produtos[chave][1]}, Preço: R${produtos[chave][2]}, Codigo: {produtos[chave][3]}, Quantidade: {produtos[chave][4]} ")
# login = int (input("\nOlá, Bem Vindo ao Sistema do Mercado!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para sistemas de clientes\nDigite 2 - para sistemas de funcionários\nEscolha aqui>>>")) 
# if login == 1:
#     cpf_cliente = int (input("Digite seu CPF: "))
#     nome_cliente = input("Digite seu Nome:")
#     escolha = int (input(f"\nOlá Cliente {nome_cliente}, Bem Vindo ao Sistema do Mercado!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para Consultar um produto\nDigite 2 - para adicionar produto ao Carrinho\nDigite 3 - para excluir produto do Carrinho\nDigite 4 - para Visualizar o carrinho\nDigite 5 - para Fechar o carrinho\nDigite 9 - para Sair\nDigite aqui:> ")) #menuzinho
#     while escolha != 9:
#         if escolha == 1:
#             busca = input("Digite o nome do produto que você quer buscar: ")
#             if busca in produtos:
#                 print(f"Produto: {busca}\nDescrição: {produtos[busca][0]}\nSubtipo: {produtos[busca][1]}\nPreço: R${produtos[busca][2]}\nCodigo: {produtos[busca][3]}\nQuantidade atual do estoque: {produtos[busca][4]}")
#             else:
#                 print("Produto não encontrado.")
#         elif escolha == 2:  
#             print("Os produtos disponiveis atualmente são:")
#             for chave in produtos:
#                 print(f"Nome: {chave}, Seção: {produtos[chave][0]}, Subtipo: {produtos[chave][1]}, Preço: R${produtos[chave][2]}, Quantidade: {produtos[chave][4]} Uni.")
# #################################################################lista para escolher produto#############################################
#             escolha_produto = input("Digite o nome do produto que você quer adicionar ao carrinho: ")
#             if escolha_produto in produtos:
#                 quantidade = int(input(f"Digite a quantidade de {escolha_produto} que você quer adicionar ao carrinho: "))
#                 if produtos[escolha_produto][4] >= quantidade:
#                     if escolha_produto in carrinho:
#                         carrinho[escolha_produto] += quantidade
#                     else:
#                         carrinho[escolha_produto] = quantidade
#                     produtos[escolha_produto][4] -= quantidade
#                     print(f"{quantidade} unidades de {escolha_produto} foram adicionadas ao carrinho.")
#                 else:
#                     print(f"Desculpe, não há quantidade suficiente de {escolha_produto} no estoque.")
#             else:
#                 print("Produto não encontrado.")
#         elif escolha == 3:
#             escolha_produto = input("Digite o nome do produto que você quer remover do carrinho: ")
#             if escolha_produto in carrinho:
#                 quantidade = int(input(f"Digite a quantidade de {escolha_produto} que você quer remover do carrinho: "))
#                 if carrinho[escolha_produto] >= quantidade:
#                     carrinho[escolha_produto] -= quantidade
#                     produtos[escolha_produto][4] += quantidade
#                     if carrinho[escolha_produto] == 0:
#                         del carrinho[escolha_produto]
#                     print(f"{quantidade} unidades de {escolha_produto} foram removidas do carrinho.")
#                 else:
#                     print(f"Você não tem essa quantidade de {escolha_produto} no carrinho.")
#             else:
#                 print("Produto não encontrado no carrinho.")
#         elif escolha == 4:
#             print("\nItens no carrinho:")
#             total = 0
#             for item, qtd in carrinho.items():
#                 preco = produtos[item][2]
#                 subtotal = preco * qtd
#                 total += subtotal
#                 print(f"{item}: {qtd} unidades, R${preco} cada, Subtotal: R${subtotal:.2f}")
#             print(f"Total a pagar: R${total:.2f}")
#         elif escolha == 5:
#             print("\nItens no carrinho:")
#             total = 0
#             for item, qtd in carrinho.items():
#                 preco = produtos[item][2]
#                 subtotal = preco * qtd
#                 total += subtotal
#                 print(f"{item}: {qtd} unidades, R${preco} cada, Subtotal: R${subtotal:.2f}")
#             print(f"Total a pagar: R${total:.2f}")
#             imposto_municipal = 0.12
#             imposto_estadual = 0.08
#             imposto_nacional = 0.05
#             total_com_imposto_municipal = total * imposto_municipal
#             total_com_imposto_estadual = total * imposto_estadual
#             total_com_imposto_nacional = total * imposto_nacional
#             total_nota_fiscal = total + total_com_imposto_municipal + total_com_imposto_estadual + total_com_imposto_nacional
#             print(f"Total de impostos: Municipal: R${total_com_imposto_municipal:.2f}, Estadual: R${total_com_imposto_estadual:.2f}, Nacional: R${total_com_imposto_nacional:.2f}")
#             print(f"Total com impostos: R${total_nota_fiscal:.2f}")
#             pagamento = int(input("\nEscolha agora a forma de pagamento!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para pagar no Dinheiro\nDigite 2 - para Pagar com PIX\nDigite 3 - para pagar com Cartão de Cred/Deb/Voucher\nDigite aqui:> "))
#             if pagamento == 1:
#                 pagamento_cliente = float(input("Qual valor pago pelo cliente? "))
#                 if pagamento_cliente >= total_nota_fiscal:
#                     troco = pagamento_cliente - total_nota_fiscal
#                     print(f"O troco a ser devolvido é: R${troco:.2f}")
#                     print("Obrigado por comprar conosco!")
#                     carrinho.clear()
#                 else:
#                     print(f"Compra não autorizada, valor pago R${pagamento_cliente:.2f} é menor que o valor total da compra! R${total_nota_fiscal:.2f}")
#                     print("Escolha outra forma de pagamento!")
#             elif pagamento == 2:
#                 pagamento_cliente = float(input("Qual o saldo existente? "))
#                 if pagamento_cliente >= total_nota_fiscal:
#                     print("Compra aprovada!!!")
#                     print("Obrigado por comprar conosco!")
#                     carrinho.clear()
#                 else:
#                     print(f"Compra não autorizada, saldo R${pagamento_cliente:.2f} é menor que o valor total da compra! R${total_nota_fiscal:.2f}")
#                     print("Escolha outra forma de pagamento!")
#             elif pagamento == 3:
#                 pagamento_cliente = float(input("Qual o saldo existente? "))
#                 if pagamento_cliente >= total_nota_fiscal:
#                     print("Compra aprovada!!!")
#                     print("Obrigado por comprar conosco!")
#                     carrinho.clear()
#                 else:
#                     print(f"Compra não autorizada, saldo R${pagamento_cliente:.2f} é menor que o valor total da compra! R${total_nota_fiscal:.2f}")
#                     print("Escolha outra forma de pagamento!")
#             else:
#                 print("Opção inválida.")
#         else:
#             print("Opção inválida.")
#         escolha = int(input("\nDigite 1 para Consultar um produto\nDigite 2 para adicionar produto ao Carrinho\nDigite 3 - para excluir produto do Carrinho\nDigite 4 - para Visualizar o carrinho\nDigite 5 - para Fechar o carrinho\nDigite 9 - para Sair\nDigite aqui:> "))
#     print("Saindo do programa...")
# ############################################################################### PERFIL FUNCIONARIO ###############################################################################
# else:
#     matricula = input ("Digite sua matricula: ")
#     nome = input ("Digite seu nome: ")
#     data_nascimento = input ("Digite sua data de nascimento: ")
#     cpf = int (input("Digite seu CPF: "))
#     escolha = int (input(f"\nOlá Funcionario {nome}, Bem Vindo ao Sistema do Mercado!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para Consultar o estoque\nDigite 2 - para Adicionar unidades a um Produto\nDigite 3 - para Excluir unidades de um produto\nDigite 4 - para Cadastrar um novo produto\nDigite 5 - para Alterar o preço de um produto\nDigite 9 - para Sair\nDigite aqui:> ")) #menuzinho
#     while escolha != 9:
#         if escolha == 1:
#             busca = input("Digite o nome do produto que você quer buscar: ")
#             if busca in produtos:
#                 print(f"Produto: {busca}\nDescrição: {produtos[busca][0]}\nSubtipo: {produtos[busca][1]}\nPreço: R${produtos[busca][2]}\nCodigo: {produtos[busca][3]}\nQuantidade atual do estoque: {produtos[busca][4]}")
#             else:
#                 print("Produto não encontrado.")
#         elif escolha == 2:
#             adicionar = input ("Digite o nome do produto para adicionar itens: ")
#             if adicionar in produtos:
#                print(f"Produto: {adicionar}\nDescrição: {produtos[adicionar][0]}\nQuantidade atual no estoque: {produtos[adicionar][4]}")
#                print("Quantos itens você quer incluir em",adicionar,"?")
#                adc = int (input ("Digite a quantidade: "))
#                soma = produtos [adicionar][4]
#                result = soma + adc
#                produtos [adicionar][4] = result
#                print (f"Foi adicionado {adc} unidades no produto {adicionar}, O estoque atualizado é: {produtos [adicionar][4]}")
#             else:
#                 print("Produto não encontrado.")
#         elif escolha == 3:
#             remover = input ("Digite o nome do produto para remover itens: ")
#             if remover in produtos:
#                 print(f"Produto: {remover}\nDescrição: {produtos[remover][0]}\nQuantidade atual no estoque: {produtos[remover][4]}")
#                 print("Quantos itens você quer remover em",remover,"?")
#                 rem = int (input ("Digite a quantidade: "))
#                 subtração = produtos [remover][4]
#                 result = subtração - rem
#                 produtos [remover][4] = result
#                 print (f"Foi removido {rem} unidades no produto {remover}, O estoque atualizado é: {produtos [remover][4]}")
#             else:
#                 print("Produto não encontrado.")       
#         elif escolha == 4:
#             nome_novo = input("Digite o nome do novo produto: ")
#             desc_novo = (input("Digite a descrição do novo produto: "))
#             tipo_novo = (input("Digite o tipo do novo produto: "))
#             preco_novo = float (input("Digite o preço do novo produto: "))
#             cod_novo = int (input("Digite o código do novo produto: "))
#             quant_novo = int (input("Digite a quantidade do novo produto: "))
#             produtos[nome_novo] = [desc_novo , tipo_novo , preco_novo , cod_novo , quant_novo]
#             print("Novo produto" , nome_novo, "adicionado com sucesso!")
#         elif escolha == 5:
#             atu_preco = input ("Digite o nome do produto para atualizar o preço: ")
#             if atu_preco in produtos:
#                 print(f"Produto: {atu_preco}\nDescrição: {produtos[atu_preco][0]}\nPreço Atual: {produtos[atu_preco][2]}")
#                 preco_new = float (input("Digite o novo preço do novo produto: "))  
#                 produtos[atu_preco][2] = preco_new
#                 print (f"O preço do produto {atu_preco} foi atualizado, O preço atual é: {produtos [atu_preco][2]}")
#             else:
#                 print("Produto não encontrado.")    
#         else:
#             print("Opção inválida.")
#         escolhab = int(input("Digite 9 para finalizar ou 0 para voltar ao MENU: "))
#         if escolhab == 9:
#             break
#         elif escolhab == 0:
#             escolha = int (input("\nOlá Funcionario, Bem Vindo ao Sistema do Mercado!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para Consultar o estoque\nDigite 2 - para Adicionar unidades a um Produto\nDigite 3 - para Excluir unidades de um produto\nDigite 4 - para Cadastrar um novo produto\nDigite 5 - para Alterar o preço de um produto\nDigite 9 - para Sair\nDigite aqui:> ")) #menuzinho
#         else:
#             print("Digite uma das opções válidas: 9 para finalizar ou 0 para voltar ao menu!")
#     print("Saindo do programa...")
########################################################################################################################################################################################################################################################################
#6.Jogo de Palavras:
# ○ Crie um jogo onde o usuário digita uma palavra e o programa verifica se ela está
# no dicionário. Se estiver, exiba seu significado.
# dicio = {"AJUDAR" : "prestar socorro" , "BARATAR" : "negociar por dinheiro" , "CHEGAR" : "alcançar ou tocar um determinado ponto no espaço ou no tempo" , "DECLARAR" : "tornar público"}
# tradu = input("Digite a palavra para traduzir: ")
# if tradu in dicio:
#     print(f"A tradução para o termo buscado é: {dicio[tradu]}")
# else:
#     print("A palavra buscada não esta no Dicionário!")
# print("Saindo....")
########################################################################################################################################################################################################################################################################
#7.Dicionário de Sinônimos:
# ○ Crie um dicionário com algumas palavras e seus sinônimos. Peça ao usuário
# para digitar uma palavra e exiba seus sinônimos
# sinonimos = {"AJUDAR" : "prestar socorro" , "BARATAR" : "negociar por dinheiro" , "CHEGAR" : "alcançar ou tocar um determinado ponto no espaço ou no tempo" , "DECLARAR" : "tornar público"}
# tradu = input("Digite a palavra para traduzir: ")
# if tradu in sinonimos:
#     print(f"A tradução para o termo buscado é: {sinonimos[tradu]}")
# else:
#     print("A palavra buscada não esta no Dicionário!")
# print("Saindo....")
########################################################################################################################################################################################################################################################################
#8.Contagem de Letras:
# ○ Leia um texto e conte quantas vezes cada letra aparece. Armazene as letras e
# suas contagens em um dicionário.
contagem = {}
