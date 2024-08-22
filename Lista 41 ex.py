#1. Crie um programa que leia 2 números inteiros e 1 real. Calcule e mostre: o produto do primeiro com a metade do segundo, a soma do triplo do primeiro com o terceiro. O terceiro número digitado ao cubo.
# numint1 = int(input("Digite o primeiro número inteiro: "))
# numint2 = int(input("Digite o segundo número inteiro: "))
# numreal = float(input("Digite o número real: "))
# produto = numint1 * (numint2/2)
# soma = (numint1*3) + numreal
# cubo = numreal ** 3 
# print("O produto do primeiro com a metade do segundo é:", produto)
# print("A soma do triplo do primeiro com o terceiro é:", soma)
# print("O cubo do terceiro número é:", cubo)
############################################################################################################
#2. Crie um programa que receba um número inteiro e verifique se ele é maior que 10 se sim, imprima: é maior que 10, senão imprima: é menor que 10.
# num = int (input("Digite o numero: "))
# if num > 10:
#     print("é maior que 10!")
# elif num == 10:
#     print ("nem maior e nem menor, é exatamente 10!")
# else: 
#     print("é menor que 10!")
#############################################################################################################
#3. Crie um programa que receba dois números e mostre qual deles é o maior.
# num1 = float (input("Digite o primeiro numero para comparar: "))
# num2 = float (input("Digite o segundo numero para comparar: "))
# if num1 > num2:
#     print ("O numero 1 é maior que o numero 2!")
# elif num1 == num2:
#     print("Ambos são iguais, sendo assim ninguem é maior que ninguem!")
# else:
#     print("O numero 2 é maior que o numero 1!")
###########################################################################################################
#4. Crie um programa que receba três números e mostre-os se estão em ordem crescente.
# num1 = input ("Digite o primeiro numero: ")
# num2 = input ("Digite o segundo numero: ")
# num3 = input ("Digite o terceiro numero: ")
# if num1 < num2 <num3 :
#     print ("Estão em ordem crescente!")
# else:
#     print ("Não estão em ordem crescente!")
###########################################################################################################
#5. Crie um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva: F - Feminino, M – Masculino ou Sexo Inválido.
# letra = input ("Digite a letra para consultar: ")
# if letra == "F" :
#     print("F - Feminino")
# elif letra == "M":
#     print("M - Masculino")
# else :
#     print("Sexo Inválido")
##########################################################################################################
#6. Crie um Programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou V- Vespertino ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# turno = input ("Digite o turno que você estuda, digite> M - Matutino, V- Vespertino ou N - Noturno > " )
# if turno == "M":
#     print("Bom Dia!")
# elif turno== "F":
#     print("Boa Tarde")
# elif turno == "N":
#     print("Boa Noite")
# else:
#     print("Valor Inválido!")
################################################################################################################
#7. Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, Crie um algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.
# valorcompra = float (input ("Digite o valor do produto: "))
# venda = 0
# if valorcompra < 50.0 :
#     venda = (valorcompra * 0.45) + valorcompra
# else:
#     venda = (valorcompra * 0.3) + valorcompra
# print("O valor de venda é: ", venda)
#########################################################################################################
#8. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
# num = float (input("Digite o numero: "))
# import math
# if num > 0:
#     raiz_quadrada = math.sqrt(num)
#     print ("A raiz quadrada é: ", raiz_quadrada)
# elif num == 0:
#     print("O numero é zero!")
# else :
#     print ("não da pra calcular negativo!")
##########################################################################################################
# 9. Crie um programa que leia dois números. Após a leitura, inverta o valor delas e mostre as mesmas com os valores invertidos.
# num1 = input("Digite o primeiro número: ")
# num2 = input("Digite o segundo número: ")
# import time
# print("Primeiro número:", num1)
# print("Segundo número:", num2)
# print("AGORA VAMOS INVERTER!!!!")
# time.sleep (1)
# print("Carregando.....")
# time.sleep (1)
# print("Calma po .....")
# time.sleep (1)
# print ("Ta carregando po .....")
# time.sleep (1)
# print ("TRAVOU .....")
# time.sleep (5)
# print ("É TROLLAGI")
# time.sleep (1)
# print ("AGORA VAI .....")
# time.sleep (1)
# print ("CALMA AE .....")
# time.sleep (1)
# print ("FOOOI .....")
# #Inverte os valores
# num1, num2 = num2, num1
# print("Primeiro número:", num1)
# print("Segundo número:", num2)
###########################################################################################################
#10. Crie um programa que leia um número inteiro e, caso ele seja positivo, calcule e mostre: • O número digitado ao quadrado;• A raiz quadrada do número digitado;
# num = int (input ("Digite o numero: "))
# import math
# if num > 0 :
#     print("O numero digitado ao quadrado é: ", num*num) #ou ele **2)
#     raiz_quadrada = math.sqrt(num)
#     print("A Raiz quadrada do numero digitado é: ", raiz_quadrada)
# else :
#     print("O numero não é positivo!!!!")
#############################################################################################################
#11. Crie um programa que receba um número inteiro e verifique se este número é par ou ímpar.
# num = int (input ("Digite o numero: "))
# if num % 2 == 0 :
#     print("Este número é PAR! ")
# else :
#     print("Este número é IMPAR! ")
#############################################################################################################
#12. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
# num1 = int (input ("Digite o primeiro numero: "))
# num2 = int (input ("Digite o segundo numero: "))
# if num1 > num2 :
#     print("O Primeiro numero é maior que o Segundo numero!")
#     print("A diferença entre eles é de:" , num1-num2)
# elif num2 > num1 :
#     print("O Segundo numero é maior que o Primeiro numero!")
#     print("A diferença entre eles é de:" , num2-num1)
# else :
#     print("Os numeros são iguais!!!!!")
###########################################################################################################
#13. Crie um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem: Números iguais.
# num1 = (input ("Digite o primeiro numero: "))
# num2 = (input ("Digite o segundo numero: "))
# if num1 > num2 :
#     print("O Primeiro numero é maior que o Segundo numero!")
# elif num2 > num1 :
#     print("O Segundo numero é maior que o Primeiro numero!")
# else :
#     print("Os numeros são iguais!!!!!")
###########################################################################################################
#14. Receba 3 números inteiros na entrada e imprima: crescente, se eles forem dados em ordem crescente. Caso contrário, imprima não está em ordem crescente.
# num1 = int (input ("Digite o primeiro numero: "))
# num2 = int (input ("Digite o segundo numero: "))
# num3 = int (input ("Digite o terceiro numero: "))
# if num1 < num2 <num3 :
#     print ("Crescente!")
# else:
#     print ("Não está em ordem crescente")
############################################################################################################
#15. Crie um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve será informado ao usuário e o programa termina.
# nota1 = float (input("Digite a primeira nota: "))
# nota2 = float (input("Digite a segunda nota: "))
# if nota1 > 0 and nota2 > 0 :
#     if nota1 <11.0 and nota2 < 11.0 :
#         print("A média é: ", (nota1 + nota2) / 2)
#     else :
#         print ("Notas invalidas, tem que ser notas maiores que 0 e menores que 10.0!")
# else :
#     print ("Notas invalidas, tem que ser notas maiores que 0 e menores que 10.0!")
#############################################################################################################
#16. Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários acima de R$ 2500,00. Dado o número de horas trabalhadas por um funcionário, informar o valor do seu salário líquido.
# horas = float (input("Informe as horas trabalhadas: "))
# valor_hora = 40.50
# bruto = horas * valor_hora
# if bruto > 2500:
#     total = bruto - (bruto * 0.11)
# else:
#     total = bruto
# print ("O Salario liquido é: ",total)
############################################################################################################
#17. Seu João precisa fazer um empréstimo automático no aplicativo, o banco aprova a transação de acordo com as seguintes condições: Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
# salario = float (input ("Digite seu salario: "))
# prestacao = float (input ("Digite o valor da prestação: "))
# porcentagem = salario * 0.2
# if prestacao > porcentagem:
#     print ("Empréstimo não concedido!!!")
# else:
#     print ("Empréstimo concedido!!!")
############################################################################################################
#18. Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde h corresponde à altura):• Homens: (72.7∗ h)−58• Mulheres: (62,1∗ h)−44,7
# altura = float (input ("Digite a altura: "))
# sexo = input ("Digite o sexo sendo M para masculino e F para feminino! > ")
# if sexo == "M":
#     peso_ideal = (72.7 * altura) - 58
#     print ("O Peso ideal é: " , peso_ideal)
# elif sexo == "F":
#     peso_ideal = (62.1 * altura) - 44.7
#     print ("O peso ideal é: ", peso_ideal)
# else:
#     print ("Digite um sexo valido! Ou digite M para masculino ou digite F para feminino!")
############################################################################################################
#19. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa termina com a mensagem “Número inválido”.
# numero = input ("Digite um número inteiro: ")
# if numero > "0":
#     print (sum (int (i) for i in numero))
# else:
#     print ("Numero Invalido!")
###############################################################################################################
#20. Crie um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.
# nota1 = float (input("Digite a primeira nota: "))
# nota2 = float (input("Digite a segunda nota: "))
# nota3 = float (input("Digite a terceira nota: "))
# media = (nota1 + nota2 + (nota3 * 2)) / 4
# print (media)
# if media >= 60.0:
#     print("Aprovado!!!!")
# else :
#     print("Reprovado")
###############################################################################################################
#21. A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi aprovado. Crie todas as verificações necessárias.
# nota1 = float (input("Digite a nota do Trabalho de Laboratorio: "))
# nota2 = float (input("Digite a nota da Avaliação Semestral: "))
# nota3 = float (input("Digite a nota do Exame Final: "))
# media = ((nota1*2) + (nota2*3) + (nota3 * 5)) / 10
# print ("A média foi: " , media)
# if media >= 0 and media <=2.9 :
#     print("Reprovado!!!!")
# elif media >= 3 and media <= 5.9:
#     print("Recuperação!!!")
# else :
#     print("Aprovado!!!")
###################################################################################################################
#22. Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.
# num = int (input("Digite o numero: "))
# match num:
#     case 1:
#         print("O Dia é Domingo!!!")
#     case 2:
#         print("O Dia é Segunda-Feira!!!")
#     case 3:
#         print("O Dia é Terça-Feira!!!")
#     case 4:
#         print("O Dia é Quarta-Feira!!!")
#     case 5:
#         print("O Dia é Quinta-Feira")
#     case 6:
#         print("O dia é Sexta-Feira")
#     case 7:
#         print("O Dia é Sabado!!!")
#     case _:
#         print("Digite um valido entre 1-7")
############################################################################################################################
#23. Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este número. Isto e, janeiro se é 1, fevereiro é 2, e assim por diante.
# num = int (input("Digite o numero: "))
# match num:
#     case 1:
#         print("O Mês é Janeiro")
#     case 2:
#         print("O Mês é Fevereiro")
#     case 3:
#         print("O Mês é Março")
#     case 4:
#         print("O Mês é Abril")
#     case 5:
#         print("O Mês é Maio")
#     case 6:
#         print("O Mês é Junho")
#     case 7:
#         print("O Mês é Julho")
#     case 8:
#         print("O Mês é Agosto")
#     case 9:
#         print("O Mês é Setembro")
#     case 10:
#         print("O Mês é Outubro")
#     case 11:
#         print("O Mês é Novembro")
#     case 12:
#         print("O Mês é Dezembro")
#     case _:
#         print("Digite um valido entre 1-12")
#############################################################################################################################
#24. Crie um programa que calcule e mostre a área de um trapézio. Sabe-se que:
# basemaior = float (input ("Digite a base maior: "))
# basemenor = float (input ("Digite a base menor: "))
# altura = float (input("Digite a altura: "))
# if basemaior > 0 and basemenor > 0 :
#         area = ((basemaior+basemenor) * altura) / 2
#         print("A Area é: ", area)
# else :
#     print("Digite bases validas, se não vai calcular!")
##########################################################################################################################
#25. Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e finalizando o programa.
# print("Bem Vindo a Calculadora Phyton!!!!!\nDigite os numeros que você quer fazer calculos:")
# num1 = int (input ("Digite o primeiro numero: "))
# num2 = int (input ("Digite o segundo numero: "))
# escolha = input ("Para Somar digite 1;\nPara Subtrair Digite 2;\nPara Dividir o primeiro pelo segundo digite 3;\nPara Multiplicar digite 4\nEscolha agora:")
# match escolha:
#     case "1" :
#         resultado = num1 + num2
#         print("A soma é: ", resultado)
#     case "2" :
#         resultado = num1 - num2
#         print("A subtração é: ", resultado)
#     case "3" :
#         resultado = num1 / num2
#         print ("O resultado da divisão é: ", resultado)
#     case "4" :
#         resultado = num1 * num2
#         print ("O Resultado da multiplicação é: ", resultado)
#     case "_" :
#         print("Digite uma das opções validas!!!! 1-Soma, 2-Subtração, 3-Divisão, 4-Multiplicação")
#######################################################################################################################################
#26.	Determine se um determinado ano lido é bissexto. Sendo que um ano e bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996.
# ano = int (input("Digite o ano para consultar: "))
# if ano % 4 == 0:
#     if ano % 100 == 0:
#         if ano % 400 == 0:
#             print(f"O ano {ano} é bissexto.")
#         else:
#             print(f"O ano {ano} não é bissexto.")
#     else:        
#         print(f"O ano {ano} é bissexto.")
# else:
#     print(f"O ano {ano} não é bissexto.")
################################################################################################################################################################################################################
#27.	Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
#•	O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
#•	Chama-se equilátero o triângulo que tem três lados iguais.
#•	Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
#•	Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
# ladoa = float (input("Digite o valor do lado A: "))
# ladob = float (input("Digite o valor do lado B: "))
# ladoc = float (input("Digite o valor do lado C: "))

# if ladoa < (ladob+ladoc) or ladob < (ladoa + ladoc) or ladoc < (ladoa + ladob): #compara se é triangulo
#     if ladoa == ladob == ladoc:
#         print("O Triângulo é Equilátero")
#     elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
#         print("O Triângulo é Isósceles")
#     else:
#         print("O Triangulo é Escaleno")
# else:
#     print("Não é um Triângulo!")
################################################################################################################################################################################################################
#28.	Crie um programa de uma calculadora simples com as 4 operações básicas, apresente o menu de opções abaixo, leia dois números reais. Em seguida mostre o resultado da operação entre os dois números recebidos. Escreva uma mensagem de erro se a opção for inválida.
# Escolha a opção:
# 1-	Soma de 2 números.
# 2-	Diferença entre 2 números (maior pelo menor).
# 3-	Produto entre 2 números.
# 4-	Divisão entre 2 números (o denominador não pode ser zero).
# print("Bem Vindo a Calculadora Phyton!!!!!\nDigite os numeros que você quer fazer calculos:")
# num1 = float (input ("Digite o primeiro numero: "))
# num2 = float (input ("Digite o segundo numero: "))
# escolha = input ("Escolha a opção:\n1-	Soma de 2 números.\n2-	Diferença entre 2 números (maior pelo menor).\n3-	Produto entre 2 números.\n4-	Divisão entre 2 números (o denominador não pode ser zero).\nEscolha: ")
# match escolha:
#     case "1" :
#         resultado = num1 + num2
#         print("A soma é: ", resultado)
#     case "2" :
#         if num1 > num2: 
#             resultado = num1 - num2
#             print("A subtração é: ", resultado)
#         elif num2 > num1:
#             resultado = num2 - num1
#             print("A subtração é: ", resultado)
#         else:
#             print("Somente subtraimos se um deles for maior, numeros iguais não apresentamos resutlado.")
#     case "3" :
#         resultado = num1 * num2
#         print ("O Resultado da multiplicação é: ", resultado)
#     case "4" :
#         if num2 != 0:
#             resultado = num1 / num2
#             print ("O resultado da divisão é: ", resultado)
#         else:
#             print("o denominador não pode ser zero")
#     case "_" :
#         print("Digite uma das opções validas!!!! 1-Soma, 2-Subtração, 3-Divisão, 4-Multiplicação")
###################################################################################################################################################################################
#29.	Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são:
# •	Ter pelo menos 65 anos,
# •	Ou ter trabalhado pelo menos 30 anos,
# •	Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
# idade = int (input("Digite a idade do trabalhador: "))
# tempo = int (input("Digite o tempo de serviço do trabalhador: "))
# if idade >= 65:
#     print ("Voce pode se aposentar, parabens!!!!")
# elif tempo >=30:
#     print ("Voce pode se aposentar, parabens!!!!")
# elif idade >= 60 and tempo >= 25:
#     print ("Voce pode se aposentar, parabens!!!!")
# else:
#    print ("Voce não pode se aposentar, F") 
###################################################################################################################################################################################
#30.	Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
# valor =  float (input ("Digite o valor do produto: R$"))
# estado = input("Digite o estado para calculo do imposto: ")
# match estado:
#     case "MG":
#         resultado = valor + (valor*0.07)
#         print("O Valor do produto com imposto é: R$",resultado)
#     case "SP":
#         resultado = valor + (valor*0.12)
#         print("O Valor do produto com imposto é: R$",resultado)
#     case "RJ":
#         resultado = valor + (valor*0.15)
#         print("O Valor do produto com imposto é: R$",resultado)
#     case "MS":
#         resultado = valor + (valor*0.08)
#         print("O Valor do produto com imposto é: R$",resultado)
#     case _ :
#         print("Digite um dos estados validos e com letra maiuscula!!! Ex.: MG, SP, RJ, MS ")
###############################################################################################################################################################################################
#31.	Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
# distancia =  float (input ("Digite a quantidade de Km: "))
# litros = float (input("Digite os litros de gasolina:  "))
# consumo = distancia / litros
# if consumo < 8:
#     print("Venda o carro!")
# elif consumo >= 8 and consumo <=14:
#     print ("Econômico!")
# else:
#     print ("  Super econômico!")
########################################################################################################################################################################
#32.	Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
# idade = int (input ("Digite a idade do nadador: "))
# if idade >= 5 and idade < 12:
#     print("Infantil")
# elif idade >= 12 and idade <= 17:
#     print("Juvenil")
# elif idade > 18:
#     print("Sênior")
# else:
#     print("Não classificado em nenhuma categoria!")
########################################################################################################################################################################
#33.	Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão abaixo:
# codigo = int (input ("Digite o codigo do produto: "))
# quant = int (input ("Digite a quantidade do produto: "))
# hot_Dog	= 12.00
# x_salada = 18.50
# x_Bacon = 25.50
# x_Burguer =	17.00
# suco_de_Laranja = 9.50
# refrigerante = 6.00

# match codigo:
#     case 100:
#         print ("O valor do pedido ficou : R$", quant * hot_Dog)
#     case 102:
#         print ("O valor do pedido ficou : R$", quant * x_salada)
#     case 103:
#         print ("O valor do pedido ficou : R$", quant * x_Bacon)
#     case 104:
#         print ("O valor do pedido ficou : R$", quant * x_Burguer)
#     case 105:
#         print ("O valor do pedido ficou : R$", quant * suco_de_Laranja)
#     case 106:
#         print ("O valor do pedido ficou : R$", quant * refrigerante)
#     case _ :
#         print ("Digite um dos codigos validos!!!")
########################################################################################################################################################################
#34.	Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela).
# preco = float (input ("Digite o preço do produto: "))
# if preco <= 50:
#     novo_preco = preco + (preco*0.05)
#     print ("O novo preço é: " , novo_preco)
# elif preco > 50 and preco <= 100:
#     novo_preco = preco + (preco*0.10)
#     print ("O novo preço é: " , novo_preco)
# else:
#     novo_preco = preco + (preco*0.15)
#     print ("O novo preço é: " , novo_preco)
########################################################################################################################################################################
#35.	Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:
# vendas = float (input ("Digite o valor da venda: R$"))
# if vendas >= 100000 :
#     comissao = 700 + (vendas * 0.16)
#     print ("O valor da comissão é: R$" , comissao)
# elif vendas < 100000 and vendas >= 80000 :
#     comissao = 650 + (vendas * 0.14)
#     print ("O valor da comissão é: R$" , comissao)
# elif vendas < 80000 and vendas >= 60000 :
#     comissao = 600 + (vendas * 0.14)
#     print ("O valor da comissão é: R$" , comissao)
# elif vendas < 60000 and vendas >= 40000 :
#     comissao = 550 + (vendas * 0.14)
#     print ("O valor da comissão é: R$" , comissao)
# elif vendas < 40000 and vendas >= 20000 :
#     comissao = 500 + (vendas * 0.14)
#     print ("O valor da comissão é: R$" , comissao)
# else:
#     comissao = 400 + (vendas * 0.14)
#     print ("O valor da comissão é: R$" , comissao)
########################################################################################################################################################################
#36.	Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela´ que considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente maior do que os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional de salário. Crie um programa que leia:
#•	o valor do salário atual do funcionário;
#•	o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).
#Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.
# salario = float (input ("Digite o valor do salario: R$"))
# tempo = int (input ("Digite o tempo de serviço: "))
# bonus = 0
# if salario <= 500 :
#     novo_salario = salario + (salario*0.25)
#     if tempo < 1 :
#         print("Valor do bonus é: R$0,00")
#     print ("O valor do novo salario é: R$" , novo_salario , "\nSomando o bonus da um total de: R$" , novo_salario+bonus)
# elif salario <= 1000 :
#     novo_salario = salario + (salario*0.20)
#     if tempo >= 1 and tempo <=3:
#         print("Tera um bonus de R$100,00")
#         bonus = 100
#     else:
#         print("Valor do bonus é: R$0,00")
#     print ("O valor do novo salario é: R$" , novo_salario , "\nSomando o bonus da um total de: R$" , novo_salario+bonus)
# elif salario <= 1500 :
#     novo_salario = salario + (salario*0.15)
#     if tempo >= 4 and tempo <=6:
#         print("Tera um bonus de R$200,00")
#         bonus = 200
#     else:
#         print("Valor do bonus é: R$0,00")
#     print ("O valor do novo salario é: R$" , novo_salario , "\nSomando o bonus da um total de: R$" , novo_salario+bonus)
# elif salario <= 2000 :
#     novo_salario = salario + (salario*0.10)
#     if tempo >= 7 and tempo <= 10:
#         print("Tera um bonus de R$300,00")
#         bonus = 300
#     else:
#         print("Valor do bonus é: R$0,00")
#     print ("O valor do novo salario é: R$" , novo_salario , "\nSomando o bonus da um total de: R$" , novo_salario+bonus)
# else : 
#         if tempo > 10:
#             print("Valor do bonus é: R$500")
#             bonus = 500
#         else:
#             print("Valor do bonus é: R$0,00")
# novo_salario = salario
# print ("O valor do novo salario é: R$" , novo_salario , "\nSomando o bonus da um total de: R$" , novo_salario+bonus)
########################################################################################################################################################################
#37.	O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.
#teste
# custo_fabrica = float(input("Digite o valor do veiculo: R$"))
# if custo_fabrica <= 12000 :
#     custo_consumidor = custo_fabrica + (custo_fabrica*0.05) + 0
#     print("O valor do carro é: R$", custo_consumidor)
# elif custo_fabrica > 12000 and custo_fabrica <= 25000:
#     custo_consumidor = custo_fabrica + (custo_fabrica*0.1) + (custo_fabrica*0.15)
#     print("O valor do carro é: R$", custo_consumidor)
# else :
#     custo_consumidor = custo_fabrica + (custo_fabrica*0.15) + (custo_fabrica*0.20)
#     print("O valor do carro é: R$", custo_consumidor)
########################################################################################################################################################################
#38.	Crie um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:
# imc = float (input ("Digite o IMC para ser calculado: "))
# if imc < 18.5 :
#     print ("Abaixo do Peso")
# elif imc >= 18.5 and imc <= 24.9:
#     print ("Saudável")
# elif imc >= 25.0 and imc <= 29.9:
#     print ("Peso em excesso")
# elif imc >= 30.0 and imc <= 34.9:
#     print ("Obesidade Grau I")
# elif imc >= 35.0 and imc <= 39.9:
#     print ("Obesidade Grau II (severa)")
# else:
#     print ("Obesidade Grau III (mórbida)")
########################################################################################################################################################################
#39Crie um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: 
#comprar apenas latas de 18 litros; 
#comprar apenas galões de 3,6 litros; 
# import math

# def calcular_tinta(area):
#     # Cálculo da quantidade de tinta necessária
#     litros_tinta = area / 6

#     # Calculando o número de latas de 18 litros e galões de 3,6 litros necessários
#     latas = math.ceil(litros_tinta / 18)
#     galoes = math.ceil(litros_tinta / 3.6)

#     # Calculando os preços
#     preco_latas = latas * 80
#     preco_galoes = galoes * 25

#     return (latas, preco_latas), (galoes, preco_galoes)

# def main():
#     try:
#         area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
#         if area <= 0:
#             raise ValueError
#         latas, preco_latas = calcular_tinta(area)[0]
#         galoes, preco_galoes = calcular_tinta(area)[1]

#         print(f"Comprando apenas latas de 18 litros: {latas} latas, Preço: R${preco_latas:.2f}")
#         print(f"Comprando apenas galões de 3,6 litros: {galoes} galões, Preço: R${preco_galoes:.2f}")
#     except ValueError:
#         print("Por favor, insira um valor válido para a área.")

# if __name__ == "__main__":
#     main()
#########################################################################################################################################################################
#40. Crie um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, Crie um programa que nos dê: 
# - salário bruto.
# - quanto pagou ao INSS.
# - quanto pagou ao sindicato.
# - o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# IR (11%)	INSS (8%)	Sindicato (5 %)

# - Salário Bruto : R$
# - Salário Líquido: R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
# def calcular_salario():
#     valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
#     horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

#     salario_bruto = valor_por_hora * horas_trabalhadas
#     desconto_ir = salario_bruto * 0.11
#     desconto_inss = salario_bruto * 0.08
#     desconto_sindicato = salario_bruto * 0.05

#     salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato

#     print("-" * 40)
#     print(f"Salário Bruto: R${salario_bruto:.2f}")
#     print(f"Desconto INSS: R${desconto_inss:.2f}")
#     print(f"Desconto Sindicato: R${desconto_sindicato:.2f}")
#     print("-" * 40)
#     print(f"Salário Líquido: R${salario_liquido:.2f}")
#     print("-" * 40)

# calcular_salario()
#########################################################################################################################################################################
#41.	Calcule as raízes da equação de 2o grau.
# Lembrando que:
 
# Onde
# ∆ = B2−4ac
# 	E ax2+ bx + c = 0 representa uma equação de 2o grau.
# A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem “Não é equação de segundo grau”.
# i.	Se ∆ < 0, não existe real. Imprima a mensagem: Não existe raiz.
# ii.	Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem: Raiz única.
# iii.	Se ∆ ≥ 0, imprima as duas raízes reais.
# import math

# def calcular_raizes(a, b, c):
#     if a == 0:
#         print("Não é uma equação de segundo grau.")
#         return
    
#     delta = b**2 - 4*a*c
    
#     if delta < 0:
#         print("Não existe raiz real.")
#     elif delta == 0:
#         raiz = -b / (2*a)
#         print(f"Raiz única: {raiz}")
#     else:
#         raiz1 = (-b + math.sqrt(delta)) / (2*a)
#         raiz2 = (-b - math.sqrt(delta)) / (2*a)
#         print(f"Raiz 1: {raiz1}")
#         print(f"Raiz 2: {raiz2}")

# # Exemplo de uso:
# a = float(input("Digite o coeficiente a: "))
# b = float(input("Digite o coeficiente b: "))
# c = float(input("Digite o coeficiente c: "))

# calcular_raizes(a, b, c)
#########################################################################################################################################################################
