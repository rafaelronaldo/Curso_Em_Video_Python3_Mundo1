nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1+nota2)/2
print("Sua média foi de {:0.2f}".format(media))
if media >=6:
    print("Sua média foi boa! PARABÉNS!")
else:
    print("Sua média foi ruim! ESTUDE MAIS!")