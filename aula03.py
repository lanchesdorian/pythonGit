# import os
# os.system("cls")
#continução input com Int e Float

#int() converte para inteiro
#float() converte para numero quebrado

# #exemplo1
# numero = 10
# numero2 = input ("digite um numero:")
# print ("o tipo do numero é,", type(numero2))
# soma = numero + int(numero2)
# print (f"soma de {numero} + {numero2}=", soma)

#exemplo2
# num1 = input("digite um numero")
# soma = float (num1) + 15
# print ("a soma de",num1, "+", "15","=", soma )

#exemplo3
# n1 = float (input("digite um numero: "))
# n2 = float (input("digite outro numero: "))
# soma = n1+n2
# print(f"soma de {n1}+{n2}=", soma)

#atividade
# n1= float (input("digite um numero:"))
# n2= float (input("digite outro numero:"))
# multiplicacao= n1*n2
# print (f"soma de {n1}*{n2}=", multiplicacao)

# num1=float(input("digite um numero:"))
# num2= num1 - 1
# num3= num1 + 1
# print("seu antecessor é" , num2)
# print("seu sucessor é ", num3)

# n1=float(input("digite seu ano de nascimento:"))
# n2= 2025 - n1
# print("sua idade é", n2)

# exemplo = float(input("digite o preço do produto:"))
# desconto = 0.15 * exemplo
# print ("o preço do produto com 15% de desconto é", exemplo-desconto)


print ("***MERCADINHO***")
produto = input("digite o produto: ")
preço = float(input ("digite o preço produto: "))
produto2 = input("digite outro produto que queira: ")
preço2 = float (input ("digite o preço deste produto: "))
desconto= 0.10*preço
desconto2= 0.25 * preço2 


print("o preço do produto 1 com 10% de desconto é: ", preço - desconto )
print("o preço do produto 2 com 25% de desconto é: ", preço2 - desconto2 )
print ("valor total de sua compra:")
final1= round (preço-desconto, 2)
final2= round (preço2-desconto2, 2)
print (final1+final2)

#round (valor,qtdCasasDecimais) - faz os arredondamento dos valores



