#1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# nota = float (input("Digite a nota: "))
# while nota < 0 or nota > 10:
#     print("Digite uma nota valida!!!!")
#     nota = float (input("Digite a nota: "))
#######################################################################################################################
#2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
# nome = input ("Digite o nome: ")
# senha = input ("Digite a senha: ")
# while nome == senha :
#     print("Nome não pode ser igual a senha!!!")
#     nome = input ("Digite o nome: ")
#     senha = input ("Digite a senha: ")
# else: 
#     print("Cadastro realizado!, O Nome cadastrado é> ", nome , "A senha cadastrada é> " , senha)
#######################################################################################################################
#3 - Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm‘ ou ‘o’;
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu Nome: ")
idade = input("Digite sua Idade: ")
salario = input("Digite seu Salario: ")
sexo = input("Digite seu Sexo: ")
estado_civil = input("Digite seu Estado Civil: ")

while int (len (nome)) < 3:
    



