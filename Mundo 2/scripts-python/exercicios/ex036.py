valor_casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos_financiamento = float(input("Quantos anos de financiamento? "))
prestacao = valor_casa / (anos_financiamento * 12)
minimo = salario * 30 / 100

print("Para pagar uma casa de R${:0.2f} em {} anos".format(valor_casa, anos_financiamento), end="")
print(" a prestação será de R$ {:0.2f}".format(prestacao))
if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")
                        