primeiro_peso = float(input("Peso da 1º pessoa: "))
maior_peso = primeiro_peso
menor_peso = primeiro_peso
for contador in range (2,6):
    peso = float(input("Peso da {}º pessoa: ".format(contador)))
    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
print("O maior peso lido foi de {}Kg".format(maior_peso))
print("O menor peso lido foi de {}Kg".format(menor_peso))
