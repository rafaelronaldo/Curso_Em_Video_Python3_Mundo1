'''for contador in range(1,10):
    print(contador)
print("Fim")'''

'''c = 1
while c < 10:
    print(c)
    c += 1'''

'''for contador in range (1,5):
    numero = int(input("Digite um valor: "))
print("Fim")'''

'''numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
print("Fim")'''

'''r = "S"
while r == "S":
    numero = int(input("Digite um número: "))
    r = str(input("Quer continuar? [S/N]")).upper()
print("Fim")'''

par = 0
impar = 0
numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} números impares!".format(par, impar))

