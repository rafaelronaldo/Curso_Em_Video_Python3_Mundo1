from datetime import date
ano = int(input("Digite um ano que quer analisar: Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print("\033[32mO ano {} é BISSEXTO!\033[m".format(ano))
else:
    print("\033[31mO ano {} não é BISSEXTO!\033[m".format(ano))