primeiro_numero = int(input("Digite um número: "))
maior = primeiro_numero
menor = primeiro_numero 
numero = 0
r = "S"
while r == "S":
    numero = int(input("Digite um número: "))
    r = str(input("Deseja continuar [S/N]? ")).upper()
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
print("O maior número digitado foi {}".format(maior))
print("O menor número digitado foi {}".format(menor))

