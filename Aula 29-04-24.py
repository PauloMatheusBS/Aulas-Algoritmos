#1
# nome = input ("Digite o nome: ")
# tamanho = len(nome) #conta caracter na string
# while tamanho < 4 :  #while len(nome) < 3 :
#     print ("Digite mais que 3 caracteres para o nome!!!!")
#     nome = input ("Digite o nome: ")
#     tamanho = len(nome)
# idade = int (input ("Digite a idade: "))
# while idade < 0 or idade >150 :    
#     print ("Digite uma idade valida!!!")
#     idade = int (input ("Digite a idade: "))
# salario = float (input ("Digite o Salario: R$"))
# while salario <= 0 :
#     print ("Digite o salario valido!")
#     salario = float (input ("Digite o Salario: R$"))
# sexo = input ("Digite o sexo: ")
# while sexo != "M" and sexo != "F" and sexo!= "m" and sexo != "f":
#     print ("Digite o sexo valido!")
#     sexo = input ("Digite o sexo sendo F ou M : ")

# print ("O nome é" , nome , "A idade é " , idade , "O Salario é : R$" , salario , "O Sexo é: " , sexo)

######################################################################################################
#2
# digitados = 0
# validar = input  ("Digite um numero: ")
# while validar > "0" and validar < "50" :
#     digitados += 1
#     validar = input ("Digite mais um numero entre 0 e 50: ")
# print ("A quantidade de numeros digitados foi: " , digitados)



######################################################################################################
#3
# i = 0 
# negativo = 0 
# positivos = []
# while i < 20:
#     numero = int (input ("Digite o numero: "))
#     if numero >= 0 :
#         positivos.append (numero) 
#     else :
#         negativo = negativo + 1     
#     i += 1
# total_positivos = sum (positivos)
# print("Os positivos são: " , positivos)
# print ("A soma dos positivos é um total de : ", total_positivos ,  "   O total de numeros negativos digitados é: " , negativo)

######################################################################################################

#4
# numero = int (input ("Digite o numero: "))
# fim = int (input ("Digite o numero final de sua tabuada: "))
# i = 0 
# tabuada = []
# while i < fim :
#     i += 1 
#     tabuada.append (numero*i)
# print (tabuada)


######################################################################################################

#5
from tkinter import messagebox
print ("Nossa empresa trabalha com o seguinte catalogo!")
print ("Ate 15min - Não Cobramos \nR$9,00 por hora \nR$1,50 por hora adicional ")
tempo = float (input ("Digite o tempo de estacionamento em minutos: "))
while tempo <= 15 :
    print ("O valor não sera cobrado!!! Saia do local imediatamente!!!!")
    messagebox.showinfo("Testando", ("teste"))
    escolha = input ("digite 9 para finalizar ou 1 para tentar novamente: ")
    if escolha == "9" :
        break
    elif escolha == "1":
        tempo = float (input ("Digite o tempo de estacionamento em minutos: "))
    else :
        print ("DIGITE 1 para tentar novamente ou 9 para sair!!!!")
if  tempo > 15:
    tempo += 9.0
    while (tempo - 60) > 0:
          tempo = tempo - 60
          tempo += 1.5
    print ("O total a pagar é: R$" , tempo)
else :
    print ("O valor de estacionamento a pagar é : R$0,00")
    

#turtle
 
#messagebox.showinfo("showinfo", "Information") 