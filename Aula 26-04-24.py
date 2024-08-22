#1
from tkinter import messagebox


nome = input("Digite o nome do usuário: ") ; 
senha = input("Digite a senha: ")
while nome == senha :
    print ("ERRRO!!!!")
    # messagebox.showinfo("ERROOOOO" , ("ERROOOOO!!!!!!!!!!!!!!!!!")) 
    messagebox.askyesno ("OXI" , ("deseja testar?")) 
    if messagebox.askyesno == True :
        print ("vc escolheu sim!")
    else :
        print ("vc escolheu não!")

    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
print ("Cadastrado com sucesso!")

#####################################################################################################################
#2
# numero = int (input ("Digite o numero "))
# i = 0
# pares = []
# while i < 14:
#     i += 1
#     if numero % 2 == 0 :
#       pares.append (numero)  
#       numero = int (input ("Digite outro numero "))
#     else :
#       numero = int (input ("Digite outro numero "))
# print ("Os numeros pares entre os 15 digitados são" , pares)


#teste
# count = 0
# numeros_pares = 0
# print("Digite 15 números inteiros:")
# # Variáveis para armazenar os números pares
# par1, par2, par3, par4, par5 = 0, 0, 0, 0, 0
# par6, par7, par8, par9, par10 = 0, 0, 0, 0, 0
# par11, par12, par13, par14, par15 = 0, 0, 0, 0, 0
# while count < 15:
#     num = int(input(f"Digite o {count+1}º número: "))
#     if num % 2 == 0:
#         numeros_pares += 1
#         # Verificando qual variável usar para armazenar o número par
#         if numeros_pares == 1:
#             par1 = num
#         elif numeros_pares == 2:
#             par2 = num
#         elif numeros_pares == 3:
#             par3 = num
#         elif numeros_pares == 4:
#             par4 = num
#         elif numeros_pares == 5:
#             par5 = num
#         elif numeros_pares == 6:
#             par6 = num
#         elif numeros_pares == 7:
#             par7 = num
#         elif numeros_pares == 8:
#             par8 = num
#         elif numeros_pares == 9:
#             par9 = num
#         elif numeros_pares == 10:
#             par10 = num
#         elif numeros_pares == 11:
#             par11 = num
#         elif numeros_pares == 12:
#             par12 = num
#         elif numeros_pares == 13:
#             par13 = num
#         elif numeros_pares == 14:
#             par14 = num
#         elif numeros_pares == 15:
#             par15 = num
#     count += 1
 
# if par1 != 0 :
#     print (par1)
#     if par2 != 0:
#         print (par2)
#         if par3 !=0:
#             print (par3)
#             if par4 !=0:
#                 print (par4)
#                 if  par5 != 0 :
#                     print(par5)
#                     if par6 != 0:
#                         print (par6)
#                         if par7 != 0 :
#                             print (par7)
#                             if par8 !=0 :
#                                 print (par8)
#                                 if par9 !=0 :
#                                     print (par9)
#                                     if par10 != 0 :
#                                         print (par10)
#                                         if par11 != 0 :
#                                             print (par11)
#                                             if par12 != 0:
#                                                 print (par12)
#                                                 if par13 != 0 :
#                                                     print (par13)
#                                                     if par14 != 0 :
#                                                         print (par14)
#                                                         if par15 !=0 :
#                                                             print (par15)
# print ("noooossssaaaaa!")

#####################################################################################################################

#3
# nome = input ("Digite o nome: ")
# tamanho = len(nome)
# while tamanho < 4 :
#     print ("Digite mais que 3 caracteres para o nome!!!!")
#     nome = input ("Digite o nome: ")
# idade = int (input ("Digite a idade: "))
# while idade <= 0 or idade >=150 :    
#     print ("Digite uma idade valida!!!")
#     idade = int (input ("Digite a idade: "))
# salario = float (input ("Digite o Salario: R$"))
# while salario < 0 :
#     print ("Digite o salario valido!")
#     salario = float (input ("Digite o Salario: R$"))
# sexo = input ("Digite o sexo: ")
# while sexo != "M" and sexo != "F" :
#     print ("Digite o sexo valido!")
#     sexo = input ("Digite o sexo sendo F ou M : ")

# print ("O nome é" , nome , "A idade é " , idade , "O Salario é : R$" , salario , "O Sexo é: " , sexo)


#####################################################################################################################
#listateste = [1,2,3,4]
# listateste2 = [19,17,15,18,16,14]
# listateste [3] #posição do lista
# listateste [0:3] #intervalo de posição do lista
# listateste.append (5) #incluindo no lista
# listateste.append (input ("Digite um numero:")) #incluindo input no lista
# listateste.extend([7, 8, 9]) #inclui varios elementos juntos nas posições do lista
# print (listateste)
# listateste.remove(9) #removeu o 9 da lista, não foi a posição e sim o elemento
# print (listateste, "removeu o elemento 9")
# # listateste.remove[1] #aqui remove mas por indice
# # print (listateste, "removeu a posição 0 do lista")
# # for i in range(len(listateste)):
# #           listateste[i] = listateste[i] * 2
# listateste[1] = 10 #troca o elemento do lista
# print (listateste)
# # len (listateste) #leria quantos elementos no lista
# lista_concatenado = listateste + listateste2 #concatenando listaes
# print (lista_concatenado) #exibindo concatenado
# lista_ordenado = sorted(listateste2) #criando variavel pra ordenar
# print (lista_ordenado) #printando variavel ordenada
# pesquisa = input ("Digite um numero: ") #aqui pesquisa o valor digitado
# if pesquisa in listateste: #testa se o elemento esta no lista 
#     print ("O elemento 2 esta aqui!")
# else:
#     print ("O elemento 2 esta aqui!")
# lista_copia = list(listateste) #aqui ele copia um lista
# print (lista_copia)
# soma = sum(listateste2) #soma elementos da lista
# print (soma) 
# lista_fatiado = listateste2[1:3]
# print (lista_fatiado) #fatia intervalo
# listateste3 = [x for x in range(10)] #cria novo lista com numeros ordenados aleatorios
# print (listateste3)
# dicionario = {"a": 1, "b": 2, "c": 3}  #testando contagem chaves na lista
# tamanho = len(dicionario)
# print("O número de chaves no dicionário é:", tamanho)


# senha = input("Digite sua senha: ") #testa numerico
# if senha.isdigit():
#     print("Senha válida!")
# else:
#     print("Senha inválida!")















