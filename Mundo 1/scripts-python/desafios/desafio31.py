distancia_viagem = float(input("Qual a distancia da viagem em KM? "))
if distancia_viagem <= 200:
    preco = distancia_viagem * 0.50
else:
    preco = distancia_viagem * 0.45
print("O preço da sua passagem será de R$ {:0.2f}".format(preco))