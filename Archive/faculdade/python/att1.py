# pro1 = float (input("Digite o primeiro produto: "))
# pro2 = float (input("Digite o segundo produto: "))
# pro3 = float (input("Digite o terceiro produto: "))

# if pro1 == pro2 or pro1 == pro3 or pro2 == pro3:
#     print("Os produtos tem o mesmo preço")
# elif pro2 < pro1 and pro2 < pro3:
#     print(pro2, "é o mais barato")
# elif pro3 < pro1 and pro3 < pro2:
#     print(pro3, "é o mais barato")
# else:
#     print(pro1, "é o mais barato") 
    
#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙
  
# num1 = float (input("Digite o primeiro número: "))
# num2 = float (input("Digite o segundo número: "))
# num3 = float (input("Digite o terceiro número: "))

# if num1 >= num2 and num1 >= num3:
#     if num2 >= num3:
#         print("A ordem decrescente é:", num1, num2, num3)
#     else:
#         print("A ordem decrescente é:", num1, num3, num2)
# elif num2 >= num1 and num2 >= num3:
#     if num1 >= num3:
#         print("A ordem decrescente é:", num2, num1, num3)
#     else:
#         print("A ordem decrescente é:", num2, num3, num1)
# elif num3 >= num1 and num3 >= num2:
#     if num1 >= num2:
#         print("A ordem decrescente é:", num3, num1, num2)
#     else:
#         print("A ordem decrescente é:", num3, num2, num1)        

#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙

# LetT = (input("Digite a letra Referente ao seu turno M - (Matutino) V - (Vespertino) e N - (Noturno): ")) .upper()              

# if LetT == 'M':
#     print("Bom dia!")
# elif LetT == 'V':
#     print("Boa tarde!")
# elif LetT == 'N':
#     print("Boa noite!")
# else:
#     print("Letra inválida!") 

#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙

#sal = float (input("Digite o salário: "))

# if sal <= 280:
#     aumento = sal * 0.2
#     novo_sal = sal + aumento
#     print("O salário com aumento é de: ", novo_sal, "e o aumento foi de: ", aumento, "20%", "do salário de: ", sal)
# elif sal > 280 and sal <= 700:
#     aumento = sal * 0.15
#     novo_sal = sal + aumento
#     print("O salário com aumento é de: ", novo_sal, "e o aumento foi de: ", aumento, "15%", "do salário de: ", sal)
# elif sal > 700 and sal <= 1500:
#     aumento = sal * 0.1
#     novo_sal = sal + aumento
#     print("O salário com aumento é de: ", novo_sal, "e o aumento foi de: ", aumento, "10%", "do salário de: ", sal)
# elif sal > 1500:
#     aumento = sal * 0.05
#     novo_sal = sal + aumento
#     print("O salário com aumento é de: ", novo_sal, "e o aumento foi de: ", aumento, "5%", "do salário de: ", sal)
# else:
#     print("Salário inválido!")
 
 
  
sal = float (input("Digite o salário: "))
    
if sal <= 280:
    aumento = 0.2
elif sal > 280 and sal <= 700:
    aumento = 0.15
elif sal > 700 and sal <= 1500:
    aumento = 0.1
elif sal > 1500:
    aumento = 0.05

aumento_sal = sal * aumento
novo_sal = sal + aumento_sal
aumento = aumento * 100
print("O salário com aumento é de: ", novo_sal, "e o aumento foi de: ", aumento_sal, aumento, "do salário de: ", sal)

    
#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙

n1 = float (input("Digite a primeira nota: "))
n2 = float (input("Digite a segunda nota: "))

media = (n1 + n2) / 2

