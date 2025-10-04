qtd_menores = 0
qtd_maiores = 0
for contador in range(1,8):
    ano_nasc = int(input("Ano de Nascimento: "))
    idade = 2025 - ano_nasc
    if idade < 18:
        qtd_menores = qtd_menores + 1
    elif idade > 18:
        qtd_maiores = qtd_maiores + 1
print("Existem {} menores de idade".format(qtd_menores))
print("Existem {} maiores de idade".format(qtd_maiores))