preco = float(input("Preço das Compras: R$"))
print("""FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque: 10% de de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal)
[4] 3x ou mais no cartão: 20% de juros""")
opcao = int(input("Qual é a opção? "))
if opcao == 1:
    desconto = preco * (10/100)
    novo_preço = preco - desconto
    print("Sua compra de R${:0.2f} vai custar R${:0.2f} no final.".format(preco, novo_preço))
elif opcao == 2:
   desconto = preco * (5/100)
   novo_preço = preco - desconto
   print("Sua compra de R${:0.2f} vai custar R${:0.2f} no final.".format(preco, novo_preço))
elif opcao == 3:
    novo_preço = preco / 2
    print("Sua compra de R${:0.2f} vai custar R${:0.2f} no final.".format(preco, novo_preço))
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    juros = preco * (20/100)
    novo_preço = preco + juros
    parcelamento = novo_preço / parcelas
    print("Sua compra será parcelada em {}x de R${} COM JUROS".format(parcelas, parcelamento))
    print("Sua compra de R${:0.2f} vai custar R${:0.2f} no final.".format(preco, novo_preço))
else:
    print("Opção INVÁLIDA!. TENTE NOVAMENTE!")
      