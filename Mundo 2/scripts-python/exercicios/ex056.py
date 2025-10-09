maior_idade = 0
nome_mais_velho = ""
cont_mulheres = 0
somaidade = 0
for contador in range(1,5):
    print("---------{}º PESSOA ---------".format(contador))
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo (M/F): ")).upper().strip()
    somaidade = somaidade + idade
    media = somaidade / 4
    if idade > maior_idade and sexo == "M":
        maior_idade = idade
        nome_mais_velho = nome
    elif idade < 20 and sexo == "F":
        cont_mulheres += 1
print("A média de idade do grupo é de: {} anos".format(media))
print("O homem mais velho tem {} anos e se chama {}.".format(maior_idade, nome_mais_velho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(cont_mulheres))