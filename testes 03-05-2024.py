# #teste 01
# # def main():
# #     # Solicita os números ao usuário
# #     num1 = int(input("Digite o primeiro número inteiro: "))
# #     num2 = int(input("Digite o segundo número inteiro: "))
# #     num3 = float(input("Digite o número real: "))

# #     # Calcula o produto do primeiro com a metade do segundo
# #     produto = num1 * (num2 / 2)

# #     # Calcula a soma do triplo do primeiro com o terceiro
# #     soma = (num1 * 3) + num3

# #     # Calcula o cubo do terceiro número
# #     cubo = num3 ** 3

# #     # Exibe os resultados
# #     print("O produto do primeiro com a metade do segundo é:", produto)
# #     print("A soma do triplo do primeiro com o terceiro é:", soma)
# #     print("O cubo do terceiro número é:", cubo)

# # if __name__ == "__main__":
# #     main()

# #teste 02
# # def main():
# #     # Recebe um número inteiro do usuário
# #     numero = int(input("Digite um número inteiro: "))

# #     # Verifica se o número é maior que 10
# #     if numero > 10:
# #         print("O número é maior que 10.")
# #     else:
# #         print("O número é menor ou igual a 10.")

# # if __name__ == "__main__":
# #     main()

# #teste 03
# # def main():
# #     # Recebe dois números do usuário
# #     num1 = float(input("Digite o primeiro número: "))
# #     num2 = float(input("Digite o segundo número: "))

# #     # Verifica qual número é maior
# #     if num1 > num2:
# #         print("O primeiro número ({}) é maior que o segundo número ({})".format(num1, num2))
# #     elif num2 > num1:
# #         print("O segundo número ({}) é maior que o primeiro número ({})".format(num2, num1))
# #     else:
# #         print("Os números são iguais.")

# # if __name__ == "__main__":
# #     main()

# #teste 04
# # def main():
# #     # Recebe três números do usuário
# #     num1 = float(input("Digite o primeiro número: "))
# #     num2 = float(input("Digite o segundo número: "))
# #     num3 = float(input("Digite o terceiro número: "))

# #     # Verifica se os números estão em ordem crescente
# #     if num1 < num2 < num3:
# #         print("Os números estão em ordem crescente.")
# #     else:
# #         print("Os números não estão em ordem crescente.")

# # if __name__ == "__main__":
# #     main()

# # import math

# # def main():
# #     numero = float(input("Digite um número: "))

# #     if numero >= 0:
# #         raiz_quadrada = math.sqrt(numero)
# #         print("A raiz quadrada de {} é {:.2f}".format(numero, raiz_quadrada))
# #     else:
# #         print("O número é inválido, pois é negativo.")

# # if __name__ == "__main__":
# #     main()

# # def main():
# #     # Lê os dois números
# #     num1 = input("Digite o primeiro número: ")
# #     num2 = input("Digite o segundo número: ")

# #     # Inverte os valores
# #     num1, num2 = num2, num1

# #     # Exibe os números com os valores invertidos
# #     print("Os números com os valores invertidos são:")
# #     print("Primeiro número:", num1)
# #     print("Segundo número:", num2)

# # if __name__ == "__main__":
# #     main()

# def main():
#     # Recebe um número inteiro do usuário
#     numero = int(input("Digite um número inteiro: "))

#     # Verifica se o número é par ou ímpar
#     if numero % 2 == 0:
#         print("O número", numero, "é par.")
#     else:
#         print("O número", numero, "é ímpar.")

# if __name__ == "__main__":
#     main()

#     def calcular_salario(horas_trabalhadas):
#     valor_por_hora = 40.50
#     salario_bruto = horas_trabalhadas * valor_por_hora
    
#     if salario_bruto > 2500:
#         salario_liquido = salario_bruto - (salario_bruto * 0.11)
#     else:
#         salario_liquido = salario_bruto
    
#     return salario_liquido

# def main():
#     horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
#     salario_liquido = calcular_salario(horas_trabalhadas)
#     print("O salário líquido do funcionário é R$ {:.2f}".format(salario_liquido))

# if __name__ == "__main__":
#     main()




# # Função para calcular a média ponderada das notas
# def calcular_media(nota1, nota2, nota3):
#     media = (nota1 + nota2 + (nota3 * 2)) / 4
#     return media

# # Função para determinar se o aluno foi aprovado ou reprovado
# def verificar_aprovacao(media):
#     if media >= 60:
#         return "Aprovado"
#     else:
#         return "Reprovado"

# # Entrada das notas das provas
# nota1 = float(input("Digite a nota da primeira prova: "))
# nota2 = float(input("Digite a nota da segunda prova: "))
# nota3 = float(input("Digite a nota da terceira prova: "))

# # Calcula a média ponderada
# media = calcular_media(nota1, nota2, nota3)

# # Verifica se o aluno foi aprovado ou reprovado
# resultado = verificar_aprovacao(media)

# # Mostra o resultado
# print("Média do aluno:", media)
# print("Resultado:", resultado)


# from turtle import *
# import turtle
# forward(100)
# left(120)
# forward(100)
# forward(100)
# left(120)
# forward(100)
# forward(100)
# left(120)
# forward(100)
# turtle.exitonclick()

# import tkinter as tk
# from tkinter import messagebox

# def soma():
#     try:
#         result_label.config(text="Resultado: " + str(float(num1_entry.get()) + float(num2_entry.get())))
#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, insira números válidos.")

# def subtracao():
#     try:
#         result_label.config(text="Resultado: " + str(float(num1_entry.get()) - float(num2_entry.get())))
#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, insira números válidos.")

# def multiplicacao():
#     try:
#         result_label.config(text="Resultado: " + str(float(num1_entry.get()) * float(num2_entry.get())))
#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, insira números válidos.")

# def divisao():
#     try:
#         result_label.config(text="Resultado: " + str(float(num1_entry.get()) / float(num2_entry.get())))
#     except ZeroDivisionError:
#         messagebox.showerror("Erro", "Não é possível dividir por zero.")
#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, insira números válidos.")

# root = tk.Tk()
# root.title("Mini Calculadora")

# # Entradas para os números
# num1_label = tk.Label(root, text="Número 1:")
# num1_label.grid(row=0, column=0)
# num1_entry = tk.Entry(root)
# num1_entry.grid(row=0, column=1)

# num2_label = tk.Label(root, text="Número 2:")
# num2_label.grid(row=1, column=0)
# num2_entry = tk.Entry(root)
# num2_entry.grid(row=1, column=1)

# # Botões para as operações
# soma_button = tk.Button(root, text="Soma", command=soma)
# soma_button.grid(row=2, column=0)

# subtracao_button = tk.Button(root, text="Subtração", command=subtracao)
# subtracao_button.grid(row=2, column=1)

# multiplicacao_button = tk.Button(root, text="Multiplicação", command=multiplicacao)
# multiplicacao_button.grid(row=3, column=0)

# divisao_button = tk.Button(root, text="Divisão", command=divisao)
# divisao_button.grid(row=3, column=1)

# # Label para mostrar o resultado
# result_label = tk.Label(root, text="")
# result_label.grid(row=4, columnspan=2)

# root.mainloop()

# def fechar_janela(event):
#     janela.destroy()
 

#  def adicao(a, b):
#     return a + b

# def subtracao(a, b):
#     return a - b

# def multiplicacao(a, b):
#     return a * b

# def divisao(a, b):
#     if b == 0:
#         return "Erro: divisão por zero!"
#     else:
#         return a / b

# def mostrar_menu():
#     print("Selecione a operação desejada:")
#     print("1. Adição")
#     print("2. Subtração")
#     print("3. Multiplicação")
#     print("4. Divisão")

# def calcular(operacao, a, b):
#     if operacao == 1:
#         return adicao(a, b)
#     elif operacao == 2:
#         return subtracao(a, b)
#     elif operacao == 3:
#         return multiplicacao(a, b)
#     elif operacao == 4:
#         return divisao(a, b)
#     else:
#         return "Operação inválida!"

# def main():
#     mostrar_menu()
#     operacao = int(input("Digite o número da operação desejada: "))
#     if operacao < 1 or operacao > 4:
#         print("Operação inválida!")
#         return

#     valor1 = float(input("Digite o primeiro valor: "))
#     valor2 = float(input("Digite o segundo valor: "))

#     resultado = calcular(operacao, valor1, valor2)
#     print("O resultado da operação é:", resultado)

# if __name__ == "__main__":
#     main()

#############################################################################################################
# def eh_bissexto(ano):
#     if ano % 4 == 0:
#         if ano % 100 == 0:
#             if ano % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# # Exemplo de uso:
# ano = 2024
# if eh_bissexto(ano):
#     print(f"O ano {ano} é bissexto.")
# else:
#     print(f"O ano {ano} não é bissexto.")

# imc, imcc, ag = input("Digite os valores de IMC, IMCC e AG separados por espaço: ").split()
# print(imc, imcc, ag)
# imc, imcc, ag = map(float, input("Digite os valores de IMC, IMCC e AG separados por espaço: ").split())
# print(imc, imcc, ag)
# import time

# print (time.asctime ()) #data hora
# def area_quadrado(lado):
#     result = lado * lado
#     return result

# lado = float(input("Digite o Lado do Quadrado:"))
# imprimindo = area_quadrado(lado)
# print(imprimindo)

import tkinter as tk
from tkinter import messagebox

def mostrar_alerta():
    messagebox.showinfo("Alerta", "Este é um alerta!")

# Cria uma janela
janela = tk.Tk()
janela.title("Botão de Alerta")

# Cria um botão que mostra um alerta quando clicado
botao_alerta = tk.Button(janela, text="Clique para alerta", command=mostrar_alerta)
botao_alerta.pack(pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()


import tkinter as tk

def obter_texto():
    texto_digitado = entrada_texto.get()
    print("Texto digitado:", texto_digitado)

# Criar uma janela
janela = tk.Tk()
janela.title("Digite seu texto")

# Criar uma entrada de texto
entrada_texto = tk.Entry(janela, width=30)
entrada_texto.pack(pady=10)

# Botão para obter o texto digitado
botao_obter_texto = tk.Button(janela, text="Obter Texto", command=obter_texto)
botao_obter_texto.pack()

# Executar a janela
janela.mainloop()



import tkinter as tk
from tkinter import messagebox

def validar_informacoes():
    nome = entry_nome.get()
    idade = entry_idade.get()
    salario = entry_salario.get()
    sexo = entry_sexo.get()
    estado_civil = entry_estado_civil.get()

    if len(nome) <= 3:
        messagebox.showerror("Erro", "O nome deve ter mais de 3 caracteres.")
        return
    try:
        idade = int(idade)
        if idade < 0 or idade > 150:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "A idade deve ser um número entre 0 e 150.")
        return
    try:
        salario = float(salario)
        if salario <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "O salário deve ser um número maior que zero.")
        return
    if sexo not in ['f', 'm', 'o']:
        messagebox.showerror("Erro", "O sexo deve ser 'f', 'm' ou 'o'.")
        return
    if estado_civil not in ['s', 'c', 'v', 'd']:
        messagebox.showerror("Erro", "O estado civil deve ser 's', 'c', 'v' ou 'd'.")
        return

    messagebox.showinfo("Sucesso", "Informações validadas com sucesso!")

# Criando a janela
root = tk.Tk()
root.title("Validação de Informações")

# Criando os widgets
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, sticky=tk.W)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

label_idade = tk.Label(root, text="Idade:")
label_idade.grid(row=1, column=0, sticky=tk.W)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1)

label_salario = tk.Label(root, text="Salário:")
label_salario.grid(row=2, column=0, sticky=tk.W)
entry_salario = tk.Entry(root)
entry_salario.grid(row=2, column=1)

label_sexo = tk.Label(root, text="Sexo:")
label_sexo.grid(row=3, column=0, sticky=tk.W)
entry_sexo = tk.Entry(root)
entry_sexo.grid(row=3, column=1)

label_estado_civil = tk.Label(root, text="Estado Civil:")
label_estado_civil.grid(row=4, column=0, sticky=tk.W)
entry_estado_civil = tk.Entry(root)
entry_estado_civil.grid(row=4, column=1)

botao_validar = tk.Button(root, text="Validar", command=validar_informacoes)
botao_validar.grid(row=5, columnspan=2)

# Iniciando o loop da aplicação
root.mainloop()