nome_completo = str(input("Digite seu nome completo: "))
nome_completo_maiusculas = nome_completo.upper()
nome_completo_minusculas = nome_completo.lower()
nome_completo_total = nome_completo.replace(" ", "")
nome_completo_total = len(nome_completo_total)
lista_de_nomes = nome_completo.split()
primeiro_nome = lista_de_nomes[0]
primeiro_nome = len(primeiro_nome)

print("Nome completo em maiúsculas: {}".format(nome_completo_maiusculas))
print("Nome completo em minúsculas: {}".format(nome_completo_minusculas))
print("Quantas letras tem o nome? {}".format(nome_completo_total))
print("Quantas letras tem o primeiro nome? {}".format(primeiro_nome))
