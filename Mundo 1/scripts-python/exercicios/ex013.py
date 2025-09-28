salario = float(input("Qual é o salário do funcionário? "))
aumento = salario * (15/100)
novo_salario = salario + aumento

print("Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:0.2f}".format(salario, novo_salario))