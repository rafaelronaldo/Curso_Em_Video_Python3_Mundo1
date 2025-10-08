numero = int(input("Digite um número inteiro: "))
quantas_vezes = 0
for contador in range (1, numero + 1):
    if numero % contador == 0:
        print('\033[33m', end=' ')
        quantas_vezes += 1
    else:
        print("\033[31m",end=' ')
    print("{}".format(contador),end='')
print("\n\033[mO número {} foi divisível {} vezes".format(numero, quantas_vezes))
if quantas_vezes == 2:
    print("E por isso ele é PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")