salario = float(input("Digite seu salário: "))
if salario > 1250:
    aumento =  salario * 10/100
    novo_salario = salario + aumento
    print("O seu salário de {} com o aumento será de {}".format(salario, novo_salario))
if salario <= 1250:
    aumento = salario * 15/100
    novo_salario = salario + aumento
    print("O seu salário de {} com o aumento será de {}".format(salario, novo_salario))
    