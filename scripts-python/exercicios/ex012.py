preco_normal = float(input("Qual é o preço do produto? "))
desconto = preco_normal * (5/100)
novo_preco = preco_normal - desconto
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:0.2f}".format(preco_normal, novo_preco))