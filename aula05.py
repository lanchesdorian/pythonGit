import os
os.system("cls")
#IF ENCADEADO
#ELIF
# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO

# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))
# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")
# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade < 60:
#     print("adulto")
# else: 
#     print("IDOSO")

#replace (valor1,valor2) - substitui o valor1 pelo valor2

# nota = float(input("Digite sua primeira nota: "))
# nota1 = float(input("Digite sua segunda nota: "))
# media = (nota+nota1)/2
# print ("sua média é", media)

# if media <5:
#     print("você é burro")
# elif media >=5 or media >=6 or media ==7:
#     print ("vamo melhorar")
# elif media>7:
#     print("você está aprovadissimo!!!!")

print(r"""
      
      ░░░░░░░░░░█████████████
░░░░░░░░░███░███░░░░░░██
███░░░░░██░░░░██░██████████
████████░░░░░░████░░░░░░░██
████░░░░░░░░░░██░░██████████
████░░░░░░░░░░░███░░░░░░░░░██
████░░░░░░░░░░░██░░██████████
████░░░░░░░░░░░░████░░░░░░░░█
████░░░░░░░░░░░░░███░░████░░█
█████████░░░░░░░░░░████░░░░░█
███░░░░░██░░░░░░░░░░░░░█████
░░░░░░░░░███░░░░░░░██████
░░░░░░░░░░░██░░░░░░██
░░░░░░░░░░░░███░░░░░██
░░░░░░░░░░░░░░██░░░░██
░░░░░░░░░░░░░░░███░░░██
░░░░░░░░░░░░░░░░░██░░░█
░░░░░░░░░░░░░░░░░░█░░░█
░░░░░░░░░░░░░░░░░░██░██
░░░░░░░░░░░░░░░░░░░███ """)
print ("REFORMULAÇÃO DE SALÁRIOS")
salario = (float(input("Digite seu salario: ")))
if salario <= 2799: 
    print ("Seu salário antes do reajuste: ", salario)
    print ("Foi aplicado 20%")
    print (f"Valor do aumento: {salario * 0.20}")
    print ("Seu novo salário: ", salario + salario*0.20)

elif salario >= 2800.00 and salario<=6999.99:
    print ("Seu salário antes do reajuste: ", salario)
    print ("Foi aplicado 15%")
    print (f"Valor do aumento: {salario * 0.15}")
    print ("Seu novo salário: ", salario + salario*0.15)

elif salario >= 7000.00 and salario<=14999.99:
    print ("Seu salário antes do reajuste: ", salario)
    print ("Foi aplicado 10%")
    print (f"Valor do aumento: {salario * 0.10}")
    print ("Seu novo salário: ", salario + salario*0.10)

else:
    salario >= 7000.00
    print ("Seu salário antes do reajuste: ", salario)
    print ("Foi aplicado 5%")
    print (f"Valor do aumento: {salario * 0.05}")
    print ("Seu novo salário: ", salario + salario*0.05)
    














    







