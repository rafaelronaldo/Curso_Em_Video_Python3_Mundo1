numero = int(input("Digite um número para ver sua tabuada: "))
for contador in range(0, 11):
    resultado = numero * contador
    print("{} x {} = {}".format(numero, contador, resultado))