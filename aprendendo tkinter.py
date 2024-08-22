from tkinter import*
#import tkinter as tk #import tkinter

teste=Tk()
teste.geometry("300x700")
teste.title ("Teste")
teste.config(bg="green")
teste.mainloop()


# tela = tk.Tk() #cria a tela
# canvas = tk.Canvas(tela,width=300, height=300, relief='solid', bd=2) #altura e largura da tela e bordas
# canvas.pack(padx=3, pady=3)#borda


#                               #x1 y1   x2  y2  cordepreenchi  cordaborda
# #ret = canvas.create_rectangle(150,150,160,160,fill="black", outline="red")

# def desenhar_ponto (event):
#     coord_x = event.x
#     coord_y = event.y
#     print(f'Valor de x: {coord_x}; valor de y: {coord_y}')
#     canvas.create_rectangle(coord_x,coord_y,coord_x+2,coord_y+2,fill="black", outline="red")

# #canvas.bind("<Button-1>" , desenhar_ponto)
# canvas.bind("<B1-Motion>" , desenhar_ponto)
# tela.mainloop() #mantem a tela ativa
########################################################################################################
# import tkinter as tk

# def clique_botao():
#     print("O botão foi clicado!")

# # Criando a janela principal
# janela = tk.Tk()
# janela.title("Exemplo de Botão")
# # Definindo as dimensões da janela (largura x altura)
# largura = 400
# altura = 300
# janela.geometry(f"{largura}x{altura}")

# # Criando um botão
# botao = tk.Button(janela, text="Clique aqui", command=clique_botao)
# botao.pack(pady=20)  # Adicionando um espaçamento entre o botão e outros elementos

# # Exibindo a janela
# janela.mainloop()
##############################################################################################################
# import tkinter as tk
# from tkinter import messagebox

# def mostrar_caixa():
#     resposta = messagebox.askyesno("Confirmação", "Você quer continuar?")
#     if resposta:
#         print("Você clicou em Sim")
#     else:
#         print("Você clicou em Não")

# def teste():
#     messagebox.showinfo("Alerta", "porq vc clicou aqui?")
#     print("porq vc clicou aqui?")
    

# # Criando a janela principal
# janela = tk.Tk()
# janela.title("Caixa de teste")
# largura = 400
# altura = 300
# janela.geometry(f"{largura}x{altura}")

# # Criando um botão para mostrar a caixa de diálogo
# botao1 = tk.Button(janela, text="Mostrar Caixa de Diálogo", command=mostrar_caixa)
# botao2 = tk.Button(janela, text="Não clique!", command=teste)
# botao1.pack(pady=20)
# botao2.pack(pady=40)


# # Exibindo a janela
# janela.mainloop()
########################################################################################################################
# import tkinter as tk
# from tkinter import messagebox, simpledialog

# def exibir_confirmacao():
#     resposta = messagebox.askyesno("Confirmação", "Você tem certeza?")
#     if resposta:
#         print("Você clicou em Sim")
#     else:
#         print("Você clicou em Não")

# def exibir_informacao():
#     messagebox.showinfo("Informação", "Este é um exemplo de mensagem informativa.")

# def exibir_aviso():
#     messagebox.showwarning("Aviso", "Este é um exemplo de mensagem de aviso.")

# def exibir_erro():
#     messagebox.showerror("Erro", "Este é um exemplo de mensagem de erro.")

# def exibir_pergunta():
#     resposta = messagebox.askquestion("Pergunta", "Você gostaria de continuar?")
#     if resposta == 'yes':
#         print("Sim")
#     else:
#         print("Não")

# def exibir_entrada():
#     entrada = simpledialog.askstring("Entrada", "Digite seu nome:")
#     if entrada:
#         print("Seu nome é:", entrada)
#     else:
#         print("Nenhum nome fornecido.")

# # Criando a janela principal
# janela = tk.Tk()
# janela.title("Exemplo de Botões em Tkinter")

# # Botões
# botoes = [
#     ("Confirmar", exibir_confirmacao),
#     ("Info", exibir_informacao),
#     ("Aviso", exibir_aviso),
#     ("Erro", exibir_erro),
#     ("Pergunta", exibir_pergunta),
#     ("Entrada", exibir_entrada)
# ]

# # Adicionando botões à janela
# for texto, comando in botoes:
#     botao = tk.Button(janela, text=texto, command=comando)
#     botao.pack(pady=5)

# # Exibindo a janela
# janela.mainloop()










