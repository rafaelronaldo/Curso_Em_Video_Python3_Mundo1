numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
  print("O primeiro número {} é maior que o segundo número {}".format(numero1, numero2))
elif numero2 > numero1:
  print("O segundo número {} é maior que o primeiro número {}".format(numero2, numero1))
else:
  print("Não existe valor maior, os dois são iguais.")