velocidade = int(input("Digite a velocidade do carro: "))

if velocidade > 80:
    print("Você foi multado!")
    multa = (velocidade-80) * 7
    print("Você deve pagar uma multa de R${}!".format(multa))
else:
    print("Você não será multado!")