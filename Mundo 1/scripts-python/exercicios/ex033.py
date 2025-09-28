numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))
numero3 = float(input("Digite o terceiro número:"))
# verificando o maior
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
#Verificando quem é o maior
maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))