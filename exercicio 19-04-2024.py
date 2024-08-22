#1
#nome = input("Qual o seu nome? :")
#idade = int (input("Quantos anos você tem? :" ))
#print("Olá", nome ,", você tem " , idade , "anos")

########################################################################################################

#2
#numero = int (input("Qual o numero para avaliar? :"))
#from tkinter import * 
#from tkinter import messagebox 
  
#messagebox.showinfo("Testando Ant e Suc" , ("O Antecessor é: ", numero-1 , "o Sucessor é:" , numero+1)) 
#messagebox.showinfo("showinfo", "Information") 
#print("O Antecessor é: ", numero-1 , "o Sucessor é:" , numero+1 )

########################################################################################################

#3
#numero1 = int (input("Qual o primeiro numero para avaliar? :"))
#numero2 = int (input("Qual o segundo numero para avaliar? :"))
#numero3 = int (input("Qual o terceiro numero para avaliar? :"))
#print("A média é:", (numero1+numero2+numero3)/3 )

########################################################################################################

#4
# dia = int (input("Qual o dia que vc quer consultar? :"))
# if dia ==1 :
#   print("O dia Consultado é Segunda-Feira")
        
# elif dia ==2 :
#    print("O dia Consultado é Terça-Feira")
        
# elif dia ==3 :
#    print("O dia Consultado é Quarta-Feira")
        
# elif dia ==4 :
#    print("O dia Consultado é Quinta-Feira")
        
# elif dia ==5 :
#    print("O dia Consultado é Sexta-Feira")
        
# elif dia ==6 :
#    print("O dia Consultado é Sabado")
        
# elif dia ==7 :
#    print("O dia Consultado é Domingo") 
        
# else :
# #    print("Digite um numero de 1-7, sendo 1-Segunda, 2-Terça, ...") 
#     from tkinter import * 
#     from tkinter import messagebox 
#     messagebox.showerror("Dia não encontrado", ("Digite um numero de 1-7, sendo 1-Segunda, 2-Terça, ...")) 
    #messagebox.OK
#teste

# n = int(input("Qual o dia que vc quer consultar? :"))
# while n <= 0 or n >7:
#  n = int(input())
 
# semana = ["domingo","segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira","sábado"]
 
# dia = semana[n-1]
 
# print("O dia da semana é %s" % dia)
 




########################################################################################################

#5     
#numero = int (input("Qual o numero que vc quer consultar? :"))
#print("Seu numero é ", numero)   
#if numero ==0:
#    print("O numero é ZERO então é isso! kkkkk")
#elif numero > 0:
#    print("O numero é POSITIVO! kkkkk")
#else :
#    print("O numero é NEGATIVO! kkkkk")

########################################################################################################

#6
#numero1 = int (input("Qual o primeiro numero para avaliar? :"))
#numero2 = int (input("Qual o segundo numero para avaliar? :"))
#operacao = (input("Qual operação você quer fazer? Digite + para adição / - para subtração:"))
#if operacao == "+" :
#    print("Sua soma deu: ", numero1 + numero2)
#elif operacao == "-" : 
#    print("Sua subtração deu: ", numero1 - numero2)
#else :
#    print("Digite + ou - poha!")

#######################################################################################################

#7
#discoazul1 = 20.00
#discolaranja2 = 30.00
#discoroxo3 = 40.00
#discomarrom4 = 50.00
#consulta = (input("Qual a cor pra consultar? :" ))
#if consulta =="Azul" :
#    print("O preço do Disco Azul é: R$", discoazul1)
#elif consulta == "Laranja":
#    print("O preço do Disco Laranja é: R$", discolaranja2)
#elif consulta == "Roxo":
#    print("O preço do Disco Roxo é: R$", discoroxo3)
#elif consulta == "Marrom":
#    print("O preço do Disco Marrom é: R$", discomarrom4)
#else :
#    print("Digite uma das cores disponiveis (Azul, Laranja, Marrom, Roxo)")

#teste
#     

########################################################################################################

#8
# base = float (input("Qual a base do terreno que vc quer consultar? :"))
# if base > 0 :
#    altura = float (input("Qual a altura do terreno que vc quer consultar? :"))
#    if altura > 0 :
#         if base == altura : #aqui valida se são lados diferentes
#           print ("Nem é retangulo!, digita certo ae!!!!")
#         else :
#            print ("A Área do retangulo é: " , (base*altura))
#    else :
#        print ("Altura digitada é invalida, digita direito ae!!!!!!")
# else :
#    print("Base digitada é invalida, digita direito ae!!!!!!")

#teste com while
# validadorbase = float (input ("Qual a base do terreno que vc quer consultar? :"))

# while (validadorbase <= 0): #aqui avalia se numero digitado é menor ou igual a 0
#     print("Base digitada é invalida, digita direito ae!!!!!!")
#     validadorbase = float (input ("Qual a base do terreno que vc quer consultar? :"))#aqui ele reseta a variavel para criar loop
# if validadorbase > 0 :
#     validadoraltura = float (input ("Qual a altura do terreno que vc quer consultar? :"))
#     while (validadoraltura <= 0): #aqui avalia se numero digitado é menor ou igual a 0
#         print("Altura digitada é invalida, digita direito ae!!!!!!")
#         validadoraltura = float (input ("Qual a altura do terreno que vc quer consultar? :"))#aqui ele reseta a variavel para criar loop
#     if validadoraltura > 0 :
#         while (validadoraltura == validadorbase):
#             print("Isso nem é retangulo, confirma essas medidas direito ae!!!!!!")  
#             validadoraltura = float (input ("Qual a altura do terreno que vc quer consultar? :"))
#         if validadoraltura != validadorbase:
#             print("A área do seu retangulo é: ", (validadorbase*validadoraltura))  
        

########################################################################################################

# 9
# cavalo = int (input("Quantos cavalos ao total? :"))
# print("O numero total de ferraduras é: " , (cavalo*4))

########################################################################################################

# #10
# numero = int (input("Qual o numero para avaliar? :"))
# print ("O antecessor é:" , numero-1)

########################################################################################################

#11
# anos = int (input ("Digite sua idade em anos: "))
# meses = int (input ("Digite sua idade em meses: "))
# dias = int (input ("Digite sua idade em dias: "))
# idadedias = print ("Sua idade em dias é:" , (anos*365) + (meses*30) + dias )

########################################################################################################

#12
# numero = float (input("Digite o numero para consultar:"))
# while numero == 0:
#     print("O numero é zero, sendo assim digite um numero válido!")
#     numero = float (input("Digite o numero para consultar:"))
# if  numero > 0 :
#     print("O numero é POSITIVO!")
# elif numero < 0 :
#     print("O numero é NEGATIVO!")

########################################################################################################

#13
# tempo = input("Digite se o tempo é SOL ou CHUVA:")
# while tempo != "SOL" and tempo != "CHUVA":
#     print ("Digite um dos 2 possiveis com letra maiuscula, ou voce digita SOL ou Digita CHUVA")
#     tempo = input("Digite se o tempo é SOL ou CHUVA:")
# if tempo == "SOL":
#     print("Ir á Praia!!!")
# else :
#     print("Ler um livro!!!")

#14
# import random #biblioteca pra gerar aleatoridade

# class student : # Criada classe student
#     def __init__(self, matrícula, sexo, altura, statusFisico) -> None:  # Dentro da classe definimos INIT que faz com que sejamos capaz de dar atributos a classe.
#         self.matrícula = matrícula
#         self.sexo = sexo
#         self.altura = altura
#         self.statusFisico = statusFisico

# # Definimos variáveis para uso posterior, mesmo que elas não sejam absolutamente necessárias aqui.
# listaEstudantes = []
# mat = 0
# sexo = ""
# altura = 0
# statusFisico = 1

# quantidadeAlunas170Altura = 0
# quantidadeAlunosFisico1 = 0

# # Definimos um Método para selecionar o sexo do aluno. "Também poderiamos fazer isso para o status físico mas decidi que nível fica melhor" -
# def sexoAleatório():
#     sexo = ["Masculino","Feminino"]
#     return random.choice(sexo)

# # Primeiro criamos um loop para definir aleatóriamente as variáveis dos alunos.
# for i in range(50):
#     # Nota-se que o número da matricula inicia-se em 111.111. Puramente cosmético, isso impede que tenha números de matricula abaixo de 
#     mat = random.randint(111111,999999)
#     sexo = sexoAleatório()
#     altura = random.randint(130,220)
#     statusFisico = random.randint(1,3)
#     estudante = student(mat,sexo,altura,statusFisico)
#     listaEstudantes.append(estudante)

# for aluno, student in enumerate(listaEstudantes, start= 1):
#     print(f"Aluno {aluno}: Matricula : {student.matrícula}, sexo : {student.sexo}, altura : {student.altura} e Nivel Fisico {student.statusFisico}")
#     if student.sexo == "Feminino" and student.altura >= 171:
#         quantidadeAlunas170Altura += 1
#     if student.sexo == "Masculino" and student.statusFisico == 1:
#         quantidadeAlunosFisico1 += 1

# print("A Quantidade de alunas com altura superior mas não igual a 1.70 M é de :", quantidadeAlunas170Altura)
# print("A Quantidade de alunos homens com um bom status fisico, em porcentagem a quantia de alunos totais é de :", int((quantidadeAlunosFisico1 / 50) * 100), "%")










    
        

















   



    