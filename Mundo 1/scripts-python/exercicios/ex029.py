velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    print("MULTADO! você excedeu o limite permitido que é de 80Km/h")
    multa = (velocidade-80) * 7
    print("Você deve pagar uma multa de R${:0.2f}".format(multa))
print("Tenha um bom dia! Dirija com segurança!")