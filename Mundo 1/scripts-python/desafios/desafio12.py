preco = float(input("Digite o preço do produto: "))
desconto = preco * 5/100
novo_preco = preco - desconto

print("Valor original: {}".format(preco))
print("Novo preço com desconto: {}".format(novo_preco))