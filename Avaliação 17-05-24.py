#Uma empresa de RH....
print ("Bem Vindo ao sistema de inscrição de candidatos!!!!")
mensagem_rep = "Obrigado pela sua participação!!!!"
mensagem_apr = "Parabéns, você passou para a próxima fase!!!!, BOA SORTE!!!!"

print ("Agora vamos fazer algumas confirmações!!!!")
cargo = input("Digite o cargo pretendido do candidato: ")
nome_completo = input("Digite o nome completo do Candidato: ")
email = input("Digite o e-mail do Candidato: ")
idade = int (input("\nDigite sua idade: "))
if idade > 17:
    print(f"mensagem enviada para o e-mail{email} >>> {mensagem_apr}")
    print("Parabens, você passou na primeira fase!!!!")
    curso = input("Voce tem curso de Qualificação na área?\nSe a resposta for SIM, digite S ou digite N para não\nEscolha S ou N >")
    while curso != "S" and curso != "N":
        print("\nDigite uma das opções validas, ou digita S(Maiusculo) - para sim ou digita N(Maiusculo) - para não!")
        curso = input("Voce tem curso de Qualificação na área?\nSe a resposta for SIM, digite S ou digite N para não\nEscolha S ou N >")
    else:
        if curso == "S":
            print(f"mensagem enviada para o e-mail{email} >>> {mensagem_apr}")
            print("Parabens, você passou na segunda fase!!!!")
            print("\nAgora vamos falar sobre sua prova!")
            nota = float (input ("Qual foi a nota da sua prova: "))
            if nota > 7.0:
                print(f"mensagem enviada para o e-mail{email} >>> {mensagem_apr}")
                print("Parabens, você esta apto(a) para a fase final!!!!")
            else:
                print("Infelizmente voce foi reprovado nesta etapa, Boa Sorte na próxima!")
                print(f"mensagem enviada para o e-mail{email} >>> {mensagem_rep}")
        else:
            print("Infelizmente voce foi reprovado, Boa Sorte na próxima!")  
            print(f"mensagem enviada para o e-mail{email} >>> {mensagem_rep}")
else:
    print("Infelizmente voce foi reprovado, Boa Sorte na próxima!")
    print(f"mensagem enviada para o e-mail{email} >>> {mensagem_rep}")
print("Ate a próxima, Saindo.....")


