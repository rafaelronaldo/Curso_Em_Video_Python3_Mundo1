salario = float(input("Qual é o salário do funcionário? R$ "))
if salario > 1250:
    aumento = salario * 10 / 100
    novo_salario = salario + aumento
else:
    aumento = salario * 15 / 100
    novo_salario = salario + aumento
print("Quem ganhava R${:0.2f} passa a ganhar \033[32mR${:0.2f}\033[m agora.".format(salario, novo_salario))