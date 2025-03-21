#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙


# num = int(input("digite um numero inteiro:"))

# if num >= 1:
#     print('O número é positivo')
# elif num == 0:
#     print('O número é neutro')
# else:
#     print('O número é negativo')
    
    
#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙


# salario = float(input('Digite o salário: '))
# val_emprestimo = float(input('Digite o valor do emprestimo: '))
# parcelas = int(input('Digite a quantidade de parcelas: '))


# val_parcela = val_emprestimo / parcelas

# if val_parcela > salario * 0.3: 
#     print('Emprestimo negado')
# else:
#     print('Emprestimo aprovado')

#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙
    
    
# par_ou_impar = int(input('Digite um número inteiro: '))

# if par_ou_impar % 2 == 0:
#     print('O número é par')
# else:
#     print('O número é ímpar')
   
   
#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙 


Val_hora = float(input('Digite o valor da hora: '))
num_horas_trab = float(input('Digite o número de horas trabalhadas: '))

bruto = Val_hora * num_horas_trab

sal_min = float (1518.00)

if bruto == sal_min:
    liquido = bruto - (bruto * 0.075)
    print('O salário líquido é de', liquido)
elif bruto >= sal_min and bruto < sal_min * 2:
    liquido = bruto - (bruto * 0.09)
    print('O salário líquido é de', liquido)
elif bruto >= sal_min * 2 and bruto < sal_min * 3:
    liquido = bruto - (bruto * 0.12)
    print('O salário líquido é de', liquido)
elif bruto >= sal_min * 3:
    liquido = bruto - (bruto * 0.14)
    print('O salário líquido é de', liquido)


#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙 