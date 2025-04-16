#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙



""" Desafio: pesquisar uma maneira do usuário informar a data de nascimento

e calcular a idade deste usuário

 

Coloque o código no fórum e faça comentários do código pesquisado """



#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙


""" Neste algoritmo tentei utilizar somente operações e funções apresentadas durante a aula
para não fugir do escopo lógico do desafio. Irá apresentar idade, meses e dias vividos com
uma margem de erro para anos bissextos. """


#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙


def calcular_idade(ano_nasc, mes_nasc, dia_nasc, ano_atual, mes_atual, dia_atual):
    atual_total = ano_atual * 365 + mes_atual * 30 + dia_atual
    nascimento_total = ano_nasc * 365 + mes_nasc * 30 + dia_nasc
    dias_vividos = atual_total - nascimento_total

    anos = int(dias_vividos / 365)
    meses = int((dias_vividos % 365) / 30)
    dias = int((dias_vividos % 365) % 30)

    return {"anos": anos, "meses": meses, "dias": dias}



mes_nascimento = int(input("Informe apenas o seu mês de nascimento (número): "))
dia_nascimento = int(input("Informe apenas o seu dia de nascimento (número): "))
ano_nascimento = int(input("Informe apenas o seu ano de nascimento (número): "))


print("Você nasceu em: ", dia_nascimento, "/", mes_nascimento, "/", ano_nascimento)


mes_atual = int(input("Informe apenas o mês atual (número): "))
dia_atual = int(input("Informe apenas o dia atual (número): "))
ano_atual = int(input("Informe apenas o ano atual (número): "))

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
