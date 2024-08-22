#1
tempo = int (input ("Digite o tempo total de estacionamento: "))
total = 0
if tempo < 15:
        print ("O total a pagar é: R$", total)
else:
    total += 9.0
    while (tempo - 60) > 0:
          tempo = tempo - 60
          total += 1.5
    print ("O total a pagar é: R$" , total)
    
#2 testando vetor

