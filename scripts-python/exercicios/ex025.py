nome_completo = str(input("Digite seu nome completo: "))
nome_completo = nome_completo.upper()
nome_completo = nome_completo.strip()
print("Seu nome tem Silva? {}".format("SILVA" in nome_completo))