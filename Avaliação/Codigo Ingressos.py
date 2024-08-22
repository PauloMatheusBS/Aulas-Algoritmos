#Crie um fluxograma e o pseudocodigo que receba o nome da pessoa, receba o valor do ingresso e o tipo do ingresso (meia ou inteira), caso seja meia receba a carteirinha.
#Calcule no final o valor total da compra com todos os ingressos comprados e imprima quais os tipos de ingresso.
nome = input("Digite o seu nome: ")
total_da_compra = 0.0 #declarei float pra facilitar
tipos_de_ingressos = []

while True:
    valor_ingresso = float(input("Digite o valor do ingresso: "))
    tipo_ingresso = input("Digite o tipo do ingresso (meia ou inteira): ").strip().lower() #isso aqui é pra espaço e pra maiuscula
    if tipo_ingresso == "meia":
        carteirinha = input("Digite a carteirinha: ")
        tipos_de_ingressos.append("meia")
        total_da_compra += valor_ingresso / 2
    elif tipo_ingresso == "inteira":
        tipos_de_ingressos.append("inteira")
        total_da_compra += valor_ingresso
    else:
        print("Tipo de ingresso inválido. Por favor, digite 'meia' ou 'inteira'.")
    outro_ingresso = input("Você quer comprar outro ingresso? (sim ou não): ").strip().lower()#isso aqui é pra espaço e pra maiuscula
    if outro_ingresso == "não":
        break
print(f"\nNome: {nome}")
print(f"Total da compra: R$ {total_da_compra:.2f}") #isso aqui é pra casa decimal
print("Tipos de ingressos comprados:", ', '.join(tipos_de_ingressos)) #isso aqui é pra tratar a string porque tava dando bug entre string e lista




