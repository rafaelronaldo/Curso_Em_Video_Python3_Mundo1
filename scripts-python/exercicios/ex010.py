carteira = float(input("Quanto dinheiro você tem na carteira? R$"))
dolares = carteira / 5.32

print("Com R${} você pode comprar US${:0.2f}".format(carteira, dolares))