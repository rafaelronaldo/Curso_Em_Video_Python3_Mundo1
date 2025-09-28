numero = int(input("Me diga um número qualquer: "))
if numero % 2 == 0:
    print("\033[32mO número {} é PAR!\033[m".format(numero))
else:
    print("\033[31mO número {} é IMPAR!\033[m".format(numero))