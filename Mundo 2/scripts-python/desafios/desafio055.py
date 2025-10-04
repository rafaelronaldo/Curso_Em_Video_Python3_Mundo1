primeiro_peso = float(input("Digite o primeiro peso: "))
maior_peso = primeiro_peso
menor_peso = primeiro_peso
for contador in range(2,6):
    peso = float(input("Digite o seu peso: "))
    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
print("O maior peso foi: {}".format(maior_peso))
print("O menor peso foi {}".format(menor_peso))
    