primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Digite a razão: "))
décimo = primeiro_termo + (10 - 1) * razao
for contador in range (primeiro_termo, décimo + razao, razao):
    print(contador, end=" -> ")
print("Acabou")