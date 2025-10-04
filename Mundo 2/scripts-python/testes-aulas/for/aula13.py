for contador in range(1, 6):  # ele ignora o último
    print("Oi")
print("FIM")

for contador in range(0, 6):
    print(contador)
print("FIM")

for contador in range(1, 7):
    print(contador)
print("FIM")

for contador in range(6, 0, -1):
    print(contador)
print("FIM")

for contador in range (0, 7, 2):
    print(contador)
print("FIM")

for contador in range (10, 0, -2):
    print(contador)
print("FIM")

numero = int(input("Digite um número: "))
for contador in range (0, numero+1):
    print(contador)
print("FIM")

inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
for contador in range (inicio, fim, passo):
    print(contador)
print("FIM")

soma = 0
for contador in range (0,3):
    valor = int(input("Digite um valor: "))
    soma = soma + valor
print("O somatório de todos os valores foi {}".format(soma))