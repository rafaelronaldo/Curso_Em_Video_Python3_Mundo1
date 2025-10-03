from datetime import date
ano_nasc = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("Classificação: \033[31mMIRIM\033[m")
elif idade <= 14:
    print("Classificação: \033[32mINFANTIL\033[m")
elif idade <= 19:
    print("Classificação: \033[33mJUNIOR\033[m")
elif idade <= 25:
    print("Classificação: \033[34mSÊNIOR\033[m")
else:
    print("Classificação: \033[35mMASTER\033[m")