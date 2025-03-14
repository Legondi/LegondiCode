#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙



""" Desafio: pesquisar uma maneira do usuário informar a data de nascimento

e calcular a idade deste usuário

 

Coloque o código no fórum e faça comentários do código pesquisado """



#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙


""" 
referencias para execucão do desafio: https://www.w3schools.com/python/ref_func_map.asp

                                      https://www.w3schools.com/python/ref_string_split.asp """                   
         
                                      
#龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙龙

# data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")

# dia = map(int, data_nascimento.split('/'))

# print (dia)

dia_nascimento = input("Informe seu dia de nascimento: ")
mes_nascimento = input("Informe seu mes de nascimento: ")
ano_nascimento = input("Informe seu ano de nascimento: ")


print("Você nasceu em: ", dia_nascimento, "/", mes_nascimento, "/", ano_nascimento)


dia_atual = input("Informe o dia atual: ")
mes_atual = input("Informe o mes atual: ")
ano_atual = input("Informe o ano atual: ")

print("Estamos em: ", dia_atual, "/", mes_atual, "/", ano_atual)

diaA , mesA , anoA = int(dia_nascimento - dia_atual), int(mes_atual), int(ano_atual)