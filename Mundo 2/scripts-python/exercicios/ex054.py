from datetime import date
maioridade = 0
menoridade = 0
for contador in range(1, 8):
    ano_nasc = int(input("Em que ano a {}º pessoa nasceu? ".format(contador)))
    ano_atual = date.today().year
    idade =  ano_atual - ano_nasc
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print("Das 7 pessoas apenas {} são maiores de idade".format(maioridade))
print("Das 7 pessoas apenas {} são menores de idade".format(menoridade))

