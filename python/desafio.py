#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙



""" Desafio: pesquisar uma maneira do usuário informar a data de nascimento

e calcular a idade deste usuário

 

Coloque o código no fórum e faça comentários do código pesquisado """



#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙



dia_nascimento = int(input("Informe seu dia de nascimento: "))
mes_nascimento = int(input("Informe seu mes de nascimento: "))
ano_nascimento = int(input("Informe seu ano de nascimento: "))


print("Você nasceu em: ", dia_nascimento, "/", mes_nascimento, "/", ano_nascimento)


dia_atual = int(input("Informe o dia atual: "))
mes_atual = int(input("Informe o mes atual: "))
ano_atual = int(input("Informe o ano atual: "))

print("Estamos em: ", dia_atual, "/", mes_atual, "/", ano_atual)

atual_total = ano_atual * 365 + mes_atual * 30 + dia_atual
nascimento_total = ano_nascimento * 365 + mes_nascimento * 30 + dia_nascimento
dias_vividos = atual_total - nascimento_total

idade1 = dias_vividos / 365

simplificarA = int(idade1)

idade2 = idade1 - simplificarA

idadeMes = idade2 * 12

simplificarM = int(idadeMes)

idade3 = idadeMes - simplificarM

idadeDia = idade3 * 30

simplificarD = int(idadeDia)

#sujeito a erros de calculo, pois não foi levado em consideração os anos bissextos
print("Você tem: ", simplificarA, "anos", simplificarM, "meses", simplificarD, "dias")



#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙
