frase = str(input("Digite uma frase: "))
frase = frase.strip()
frase = frase.upper()

print("A letra A aparece {} vezes na tela".format(frase.count('A')))
print("A primeira letra A apareceu na posição {}".format(frase.find('A')+1))
print("A ultima letra apareceu na posição {}".format(frase.rfind('A')+1))