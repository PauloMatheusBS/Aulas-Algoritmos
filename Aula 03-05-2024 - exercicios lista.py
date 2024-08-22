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





