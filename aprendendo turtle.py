# A biblioteca Turtle em Python é uma ferramenta divertida e educacional para criação de gráficos vetoriais. Ela permite criar desenhos e animações de forma interativa usando um ambiente gráfico.
# Aqui estão alguns conceitos básicos sobre a biblioteca Turtle:
# Tartaruga (Turtle): No contexto da biblioteca Turtle, a tartaruga é um cursor gráfico que pode se mover pela tela para desenhar linhas e formas.
# Canvas: A tela de desenho onde a tartaruga se move e desenha é chamada de "canvas".
# Comandos básicos: A tartaruga entende comandos simples para se movimentar, desenhar e alterar suas propriedades, como cor e espessura da linha.
# Coordenadas: A tartaruga se move em um sistema de coordenadas cartesianas, onde o ponto central é o ponto (0, 0) e os eixos X e Y aumentam positivamente para a direita e para cima, respectivamente.
# Principais métodos: Alguns dos principais métodos da tartaruga incluem forward(), backward(), right(), left(), penup(), pendown(), color(), width(), entre outros.
# Desenhando formas: Com a biblioteca Turtle, você pode desenhar uma variedade de formas geométricas, como linhas, círculos, polígonos e até mesmo desenhos mais complexos.
# import tkinter as tk
# from tkinter import messagebox, simpledialog
# import turtle
# def exibir_informacao():
#     messagebox.showinfo("PARE AGORA", "AGORA FAZ O E!!!!!")
    
#     def letraE ():
#         t = turtle.Turtle()
#         t.speed(1)  #velocidade
#         largura_linha = 10

#         # Desenhar a letra "E"
#         t.penup()
#         t.goto(-200, 0)   
#         t.pendown()
#         t.width(largura_linha)
#         t.left(90)
#         t.forward(100)  
#         t.right(90)
#         t.forward(50)   
#         t.backward(50)  
#         t.right(90)
#         t.forward(50) 
#         t.left(90)
#         t.forward(50) 
#         t.backward(50)
#         t.right(90)
#         t.forward(50) 
#         t.left(90),
#         t.forward(50) 
#         turtle.done() 
    
  
    

#     letraE ()
   


# def exibir_erro():
#     messagebox.showerror("Erro", "Este é um exemplo de mensagem de erro.")


# # Criando a janela principal
# janela = tk.Tk()
# janela.title("Exemplo de Botões em Tkinter")
# largura = 400
# altura = 300
# janela.geometry(f"{largura}x{altura}")
# # Botões
# botoes = [
#     ("NÃO CLIQUE!!!!!", exibir_informacao),
#     ("tEST", exibir_erro),
# ]


# for texto, comando in botoes:
#     botao = tk.Button(janela, text=texto, command=comando)
#     botao.pack(pady=5)


# janela.mainloop()
#####################################################################################################
# import turtle

# def desenhar_logo_netflix(t, tamanho_linha, cor):
#     # Configurações iniciais
#     t.speed(2)
#     t.width(tamanho_linha)
#     t.color(cor)

#     # Desenhar a letra "N"
#     t.penup()
#     t.goto(-100, 0)
#     t.pendown()
#     t.left(90)
#     t.forward(200)
#     t.right(150)
#     t.forward(220)
#     t.left(150)
#     t.forward(200)

#     # # Desenhar o círculo
#     # t.penup()
#     # t.goto(30, 60)
#     # t.pendown()
#     # t.circle(60)

# # Configurações iniciais
# t = turtle.Turtle()
# t.hideturtle()

# # Definir tamanho da linha e cor
# tamanho_linha = 8
# cor = "red"

# # Desenhar a logo da Netflix
# desenhar_logo_netflix(t, tamanho_linha, cor)

# # Manter a janela aberta
# turtle.done()



# import turtle

# def desenhar_logo_netflix(t, tamanho_linha, cor):
#     # Configurações iniciais
#     t.speed(2)
#     t.width(tamanho_linha)
#     t.color(cor)

#     # Desenhar a letra "N"
#     t.penup()
#     t.goto(-100, 0)
#     t.pendown()
#     t.left(90)
#     t.forward(200)
#     t.right(150)
#     t.forward(220)
#     t.left(150)
#     t.forward(200)



# # Configurações iniciais
# t = turtle.Turtle()
# t.hideturtle()
# turtle.bgcolor("black")  # Definir o fundo preto

# # Definir tamanho da linha e cor
# tamanho_linha = 8
# cor = "#E50914"  # Vermelho Netflix

# # Desenhar a logo da Netflix
# desenhar_logo_netflix(t, tamanho_linha, cor)


# # Manter a janela aberta
# turtle.done()
##################################################################################################################
# import turtle

# def desenhar_flor(t, tamanho_petalas, cor_petalas):
#     # Configurações iniciais
#     t.speed(2)
#     t.width(2)

#     # Desenhar pétalas da flor
#     t.color(cor_petalas)
#     for _ in range(13):
#         t.circle(tamanho_petalas, 60)
#         t.left(120)
#         t.circle(tamanho_petalas, 60)
#         t.left(120 - 30)

#     # Desenhar o centro da flor
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
#     t.color("yellow")
#     t.begin_fill()
#     t.circle(20)
#     t.end_fill()

# # Configurações iniciais
# t = turtle.Turtle()
# t.hideturtle()

# # Definir tamanho e cor das pétalas
# tamanho_petalas = 100
# cor_petalas = "red"

# # Desenhar a flor
# desenhar_flor(t, tamanho_petalas, cor_petalas)

# # Manter a janela aberta
# turtle.done()
################################################################################################################
# import turtle
# def quadrado_com_mensagem(t, lado, escolha):
#     t.penup()
#     t.goto(-lado/2, lado/2) 
#     t.pendown()
#     resultado = escolha*escolha    
#     for _ in range(4):
#         t.forward(lado)
#         t.right(90)
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
#     t.write(resultado, align="center", font=("Arial", 12, "normal"))
# escolha = float(input("Digite o lado do quadrado: "))
# t = turtle.Turtle()
# t.speed(1)  
# t.width(3) 
# quadrado_com_mensagem(t, 200, escolha)
# turtle.done()



