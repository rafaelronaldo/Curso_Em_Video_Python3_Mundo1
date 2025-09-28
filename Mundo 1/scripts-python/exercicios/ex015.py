dias_alugados = float(input("Quantos dias alugados? "))
km_rodados = float(input("Quantos KM rodados? "))
custos_dias = dias_alugados * 60
custos_km = km_rodados * 0.15
preco_total = custos_dias + custos_km

print("O total a pagar é de R${:0.2f}".format(preco_total))