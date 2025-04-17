def calcular_idade(ano_nasc, mes_nasc, dia_nasc, ano_atual, mes_atual, dia_atual):
    atual_total = ano_atual * 365 + mes_atual * 30 + dia_atual
    nascimento_total = ano_nasc * 365 + mes_nasc * 30 + dia_nasc
    dias_vividos = atual_total - nascimento_total

    anos = int(dias_vividos / 365)
    meses = int((dias_vividos % 365) / 30)
    dias = int((dias_vividos % 365) % 30)

    return {"anos": anos, "meses": meses, "dias": dias}


def main():
    mes_nascimento = int(input("Informe apenas o seu mês de nascimento (número): "))
    dia_nascimento = int(input("Informe apenas o seu dia de nascimento (número): "))
    ano_nascimento = int(input("Informe apenas o seu ano de nascimento (número): "))

    print("Você nasceu em: ", dia_nascimento, "/", mes_nascimento, "/", ano_nascimento)

    mes_atual = int(input("Informe apenas o mês atual (número): "))
    dia_atual = int(input("Informe apenas o dia atual (número): "))
    ano_atual = int(input("Informe apenas o ano atual (número): "))

    idade = calcular_idade(ano_nascimento, mes_nascimento, dia_nascimento, ano_atual, mes_atual, dia_atual)

    print("Você tem: ", idade["anos"], "anos", idade["meses"], "meses", idade["dias"], "dias")


if __name__ == "__main__":
    main()
