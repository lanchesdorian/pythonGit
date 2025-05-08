#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)

# idade = (float (input ("qual a sua idade? ")))
# if  idade > 18:
#     print("você é maior de idade")
# else:
#     print ("você é menor de idade")


# email = (input("digite seu email: "))
# senha= (float(input("digite sua senha: ")))

# if email == "python@senai.com" and senha ==  123456:
#     print("usuário encontrado")
# else:
#     print ("email ou senha incorretos")

# print ("**APLLE(S)**")
# qtd = int(input("digite quantas maçãs irá querer: "))
# if qtd < 12 :
#     calc = qtd * 0.30
#     print("irá pagar (0.30) a unidade: ", calc)
# else:
#     calc = qtd* 0.25
#     print ("voce ira pagar (0.25 unidade): ", calc)

#upper() - converte tudo para maiúsculo
#lower() - converte tudo para minúsculo

letra = input("Digite uma letra o alfabeto: ")
if letra == "a" and "e" and "i" and "o" and "u":
    print(letra , "é uma vogal")
else:
    print(letra , "é uma consoante")

numero= float(input("Escolha um número: "))
numero1= float(input("Escolha outro número: "))
if numero>numero1 or numero1<numero:
    print(numero," é maior que:", numero1)
else:
    print(numero, "é menor que", numero1)









   

    




