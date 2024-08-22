#exemplo 
# fruits = ["Aple" , "Banana", "Cherry"]
# for x in fruits:
#     print (x)
#     if x=="Banana":
#         break
###################################################################################################################################################
# fruits = ["Aple" , "Banana", "Cherry"]
# for x in fruits:
#     print (x)
# else:
#     print ("Acabou")
###################################################################################################################################################
# for x in range (6):
#     print(x)
###################################################################################################################################################
# for x in range (2,30,3):
#     print(x)
###################################################################################################################################################
# for x in range (2,6):
#     print(x)
###################################################################################################################################################
# for x in range (1,11):
#     print(x)
###################################################################################################################################################
# for x in range (1,11,2):
#     print(x)
###################################################################################################################################################
# import time 
# num = int (input("Digite o numero para saber a tabuada: "))
# for x in range (1,11):
#     time.sleep (1)
#     print(num , "x" , x , "=" , num * x)
#     if x == 5:
#         time.sleep (5)
#         print ("TRAVOU!!!!!")
#         time.sleep (2)
#         print ("AEE VOLTOUUUU!!!!!")
#         time.sleep (1)
#         print ("PERA PO, TA COM PRESSA?????????")
#         print ("TOMA AE ENTÃO")
#         x = 6
###################################################################################################################################################
# num = [1,2,3,4,5,6,7,8,9,10]
# result = sum(num)
# print(result)
###################################################################################################################################################
# num = [1,2,3,4,5,6,7,8,9,10]
# soma = 0
# for x in num:
#     soma += x
# result = soma
# print (result)
###################################################################################################################################################
# num = [1,2,3,4,5,6,7,8,9,10]
# soma = 0
# for x in num:
#     soma += x
#     print(soma)
###################################################################################################################################################
# lista = []
# positivo = []
# negativo = []
# zeros = []
# for x in range (10):
#     lista.append(int (input ("Digite ai: ")))
# print(lista)
# for i in lista:
#     if  i > 0:
#         positivo.append (i)
#     elif  i < 0:
#         negativo.append(i)
#     else:
#         zeros.append (i)
# print ("Essa é a lista de positivos: " , positivo)
# print ("O Total de positivos são: " , len(positivo))
# print ("Essa é a lista de negativos: " , negativo)
# print ("O Total de negativos são: " , len(negativo))
# print ("Essa é a lista de zeros digitados: " , zeros)
# print ("O Total de zeros são: " , len(zeros))
#######################################################################################################################################################
#teste
# import time
# lista = []
# positivo = []
# negativo = []
# zeros = []
# for x in range (10):
#     lista.append(int (input ("Digite: ")))
# for i in lista:
#     if  i > 0:
#         positivo.append (i)
#     elif  i < 0:
#         negativo.append(i)
#     else:
#         zeros.append (i)
# import tkinter as tk
# from tkinter import messagebox
# print ("PENSANDO")
# for _ in range (10):
#     print("." , end="" , flush=True )
#     time.sleep (0.5)
# time.sleep (2)
# print ("\nEssa é a lista de positivos: " , positivo)
# print ("O Total de positivos são: " , len(positivo))
# time.sleep (2)
# print ("E os negativos?????????")
# time.sleep (2)
# print ("huummm")
# time.sleep (3)
# messagebox.showinfo("Alerta", "TRAVOU")
# messagebox.showinfo("Alerta", "TRAVOU MESMO PO, É SERIO!!!!")
# messagebox.showinfo("Alerta", "F PC")
# messagebox.showinfo("Alerta", "É ZUEIRA PO!!!!")
# print ("Essa é a lista de negativos: " , negativo)
# print ("O Total de negativos são: " , len(negativo))
# resultado = messagebox.askyesno("QUER CONTINUAR?", "QUER MESMO VER SE TEM 0??????")
# if resultado:
#     messagebox.showinfo("Resposta", "ENTÃO TA!!!")
#     print ("Essa é a lista de zeros digitados: " , zeros)
#     print ("O Total de zeros são: " , len(zeros))
# else:
#     messagebox.showinfo("Resposta", "VAI VER MESMO ASSIM!!!")
#     print ("Essa é a lista de zeros digitados: " , zeros)
#     print ("O Total de zeros são: " , len(zeros))
# fim = messagebox.askyesno("Pesquisa de satisfação!", "Gostou?")
# if fim:
#     messagebox.showinfo("Obrigado", "De nada!!!")
# else :
#     messagebox.showinfo("AFF", "Então faz melhor, aff....")
#######################################################################################################################################################
# crescendo = []
# for i in range(100, 49, -2):
#     crescendo.append(i)
# print("Decrescente" , crescendo)
# crescendo.sort()
# print("Crescente" , crescendo)
#######################################################################################################################################################
# for i in range(100 , 49 , -2):
#     print (i)
#######################################################################################################################################################
