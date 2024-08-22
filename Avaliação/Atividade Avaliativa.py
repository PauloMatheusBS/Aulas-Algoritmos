#1 - Em Python, o resultado da expressão: “2 ** 3 > 16 % 7” será:
# a) Verdadeiro
# b) Falso
# c) Null
# d) 2
# e) 8
#print(2 ** 3 > 16 % 7) #deu True = a) Verdadeiro
#####################################################################################################################################################################################################
#2 - Implemente um algoritmo em Python que receba uma string como parâmetro e imprima as
#vogais dessa string. Exemplo: string ‘univesp’ → deve imprimir os caracteres ‘u’, ‘i’ e ‘e’.
# busca = ["a","e","i","o","u","A","E","I","O","U"]
# vogais = []
# palavra = input("Digite a palavra para contagem de vogais: ")
# for i in palavra:
#     if i in busca:
#         vogais.append(i)
# vogais_encontradas = vogais
# print("As vogais dessa palavra são: " , vogais_encontradas)
####################################################################################################################################################################################################
#3 - A média harmônica amortizada é definida como:
# onde N é o número de notas a serem usadas na média, ni é a i-ésima nota, e X é o fator de
# amortização. Implemente um algoritmo em Python que calcule a média de 3 notas de um aluno
# digitadas no teclado, com fator de amortização igual a 4. Em seguida, informe se o aluno passou
# (média >= 5) ou não (média < 5).
# Exemplo de entrada:
# N1: 5.0
# N2: 10.0
# N3: 6.5
# Saída:
# Você passou, sua média é 6.8

# notas = [0,0,0]
# media_harmonica = 0
# amortizacao = 4
# n_elementos = len (notas)

# notas[0] = float (input("Digite a 1ª nota: "))
# notas[1] = float (input("Digite a 2ª nota: "))
# notas[2] = float (input("Digite a 3ª nota: "))

# soma = 0
# for elemento in notas:
#     soma += 1 / (elemento + amortizacao)

# media_harmonica = (n_elementos / soma) - amortizacao

# if media_harmonica >= 5:
#     print(f"Você passou, sua média é {media_harmonica:.1f}")
# else:
#     print(f"Você não passou, sua média é {media_harmonica:.1f}")




#######################################################################################################################################################################################################
# 4 – Faça um algoritmo que receba uma lista com 10 elementos. O algoritmo deve remover o
# elemento 8 e mostrar a lista após a remoção. O exercício deve ser feito sem utilizar as funções do
# Python de remoção.
# Exemplo de entrada:
# [5, 2, 1, 7, 9, 8, 10, 200, 12, 4]
# Exemplo de saída:
# [5, 2, 1, 7, 9, 10, 200, 12, 4]
# lista = []
# lista2 = []
# retirar = 8
# for i in range (1,11):
#     numero = input(f"Digite o {i}º Numero: ")
#     lista.append(i)
# for i in lista:
#     if i != retirar: 
#         lista2.append(i)
# print("LISTA INICIAL" , lista)    
# print("LISTA FINAL" , lista2)
##########################################################################################################################################################################################################
#5 - Num país imaginário chamado Lisarb, todas as pessoas ficam muito felizes em pagar os seus
# impostos porque sabem que não existem políticos corruptos e que os impostos são usados para
# beneficiar a população, sem qualquer apropriação indevida. A moeda deste país é o Rombus (R$).
# Leia um valor com 2 dígitos após a vírgula, equivalente ao salário de um habitante do Lisarb. Em
# seguida, imprima o valor devido que essa pessoa deverá pagar de impostos, conforme tabela abaixo:
# Salário Taxa
# 0.00 a 2.000,00 Isento 
# 2.000.01 a 3.000,00 8%
# 3.000,01 a 4.500,00 18%
# Acima de 4.500,00 28%
# Se o salário for de R$ 3.002,00 por exemplo, a alíquota de 8% é sobre R$ 1.000,00, pois o salário
# de R$ 0,00 a R$ 2.000,00 é isento de impostos. No exemplo a seguir, a alíquota total é de 8% sobre
# R$ 1.000,00 + 18% sobre R$ 2,00, resultando em R$ 80,36 ao todo. 
# Entrada:
# A entrada contém apenas um número de ponto flutuante, com 2 dígitos após o ponto decimal.
# Saída:
# Imprima a mensagem “R$” seguida de um espaço em branco e o valor total do imposto a pagar,
# com dois dígitos após a vírgula. Se o valor for até 2000, imprima a mensagem "Isento".
# Exemplo 1:
# Entrada: 3002.00 
# Saída: R$ 80.36
# Exemplo 2:
# Entrada: 1701.12
# Saída: Isento

# salario = float (input("Digite o salário: "))
# if salario <= 2000:
#     print("Isento")
# elif salario <= 3000:
#     imposto = (salario - 2000) * 0.08
#     print(f"R$ {imposto:.2f}")
# elif salario <= 4500:
#     imposto = 1000 * 0.08
#     imposto += (salario - 3000) * 0.18
#     print(f"R$ {imposto:.2f}")
# else:
#     imposto = 1000 * 0.08
#     imposto += 1500 * 0.18
#     imposto += (salario - 4500) * 0.28
#     print(f"R$ {imposto:.2f}")


