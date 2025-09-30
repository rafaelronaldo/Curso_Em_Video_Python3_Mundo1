nome = str(input("Digite seu nome: "))
if nome == "Rafael":
    print("Que nome mais lindo!")
elif nome == "Maria" or nome == "Pedro" or nome == "Lucas":
    print("Seu nome é bem popular!")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino!")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia, {}!".format(nome))
