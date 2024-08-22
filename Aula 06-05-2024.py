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