soma = 0
for contador in range (1, 7):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        soma = soma + numero
print(soma)