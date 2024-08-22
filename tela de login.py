# import tkinter

# janela = tkinter.Tk()
# janela.geometry("500x300")

# def clique ():
#     print("Clicou no Botão")

# texto = tkinter.Label(janela, text="Fazer Login")
# texto.pack(padx=10, pady=10)

# botao = tkinter.Button(janela, text="Login", command=clique)
# botao.pack(padx=10,pady=10)

# janela.mainloop()
#############################################################################################################################################################
import customtkinter


janela = customtkinter.CTk()



janela.geometry("500x300")
customtkinter.set_appearance_mode("Dark")

def clique ():
    print("Clicou no Botão")

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)


email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha")
senha.pack(padx=10, pady=10)

qualquer_coisa = customtkinter.CTkCheckBox(janela, text="Lembrar senha" )
qualquer_coisa.pack(padx=10, pady=10)



botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10,pady=10)


janela.mainloop()

