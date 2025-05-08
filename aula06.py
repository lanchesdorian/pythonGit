#SWITCH CASE 
# dia = (input("digite um número do dia da semana: "))
# match dia:
#     case "1":
#         print ("Este dia é domingo")
#     case "2":
#         print ("Este dia é segunda")
#     case "3":
#         print ("Este dia é terça")
#     case "4":
#         print ("Este dia é quarta")
#     case "5":
#         print ("Este dia é quinta")
#     case "6":
#         print("Este dia é sexta!!!")
#     case "7":
#         print("Este dia é sabado")
#     case _ :
#         print ("Este dia não existe")
# celular1 = 5000.00
# celular2 = 2500.00
# celular3 = 6999.99

# print ("**** MUNDO DO CELULAR! ****")
# print ("""*CELULARES DISPONIVEIS*: 
#        Samsung s25 265 GB: R$6999.99
#        Iphone 15: R$ 5000.00
#        Xiaomi redmi 13 pro: R$ 2500.00 """)
# d = (input("Digite o celular que você quer: "))
# frete = (input ("Digite a sigla do seu estado: "))
# match frete: 
#      case "sp":
#         frete = 10.00
#      case "mg":
#         frete = 15.00
#      case "rs":
#         frete = 20.00
# match d:
#     case "iphone 15":
#       print ("Preço: R$ 5000.00")
#       print ("O valor do frete é", frete )
#       print ("Seu total é: R$", celular1 + frete )
#     case "xiaomi redmi 13 pro":
#       print ("Preço: R$ 2500.00")
#       print ("O valor do frete é", frete )
#       print ("Seu total é: R$", celular2 + frete )
#     case "samsung s25 265 GB":
#       print ("Preço: R$ 6999.99")
#       print ("O valor do frete é", frete )
#       print ("Seu total é: R$", celular3 + frete )

import random


print("JOGO PEDRA PAPEL TESOURA")

papel = """
PAPEL
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
PEDRA
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
TESOURA
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

jogador = input("Escolha entre pedra, papel ou tesoura: ")
match jogador:
    case "pedra":
        jogador=pedra
    case "tesoura": 
        jogador =tesoura
    case "papel":
        jogador = papel

#1-> pedra , 2-> papel , 3->tesoura

maquina = random.randint(1,3)

match maquina:
    case 1:
        maquina=pedra
    case 2: 
        maquina =papel
    case 3:
        maquina =tesoura


print(f"voce escolheu  {jogador}")
print(f"maquina escolheu {maquina}")

match jogador:
    case _ if jogador == maquina:
        print("empate")
    case _ if jogador==pedra and maquina ==tesoura:
        print("Voce ganhou")
    case _ if jogador == tesoura and maquina ==papel: 
        print("Voce ganhou")
    case _ if jogador == papel and maquina ==pedra:
        print("voce ganhou")
    case _ :
        print("voce perdeu")


