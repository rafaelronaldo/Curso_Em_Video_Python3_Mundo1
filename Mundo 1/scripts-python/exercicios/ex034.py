salario = float(input("Qual é o salário do funcionário? R$ "))
if salario > 1250:
    aumento = salario * 10 / 100
    novo_salario = salario + aumento
else:
    aumento = salario * 15 / 100
    novo_salario = salario + aumento
print("Quem ganhava R${:0.2f} passa a ganhar R${:0.2f} agora.".format(salario, novo_salario))