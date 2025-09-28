distancia_viagem = float(input("Qual é a distância da sua viagem? "))
print("Você está prester a começar uma viagem de {}Km".format(distancia_viagem))
if distancia_viagem <=200:
    preco = distancia_viagem * 0.50
else:
    preco = distancia_viagem * 0.45
print("E o preço da sua passagem será de \033[32mR${:0.2f}\033[m".format(preco))