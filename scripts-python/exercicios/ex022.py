nome_completo = str(input("Digite seu nome completo: "))
nome_completo_maisculas = nome_completo.upper()
nome_completo_minusculas = nome_completo.lower()
nome_completo_ao_todo = nome_completo.replace(" ", "")
nome_completo_ao_todo = len(nome_completo_ao_todo)
lista_de_nomes = nome_completo.split()
primeiro_nome = lista_de_nomes[0]
primeiro_nome = len(primeiro_nome)

print("Nome completo em maiúsculas: {}".format(nome_completo_maisculas))
print("Nome completo em minúsculas: {}".format(nome_completo_minusculas))
print("Quantas letras tem: {}".format(nome_completo_ao_todo))
print("Quantas letras tem o primeiro nome: {}".format(primeiro_nome))