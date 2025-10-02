ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nasc
idade_alistamento = 18


print("Sua idade é de {}.".format(idade))
if idade < idade_alistamento:
  tempo = idade_alistamento - idade
  print("E falta {} anos para você se alistar.".format(tempo))
if idade == idade_alistamento:
  print("E está na hora de se alistar!")
elif idade > idade_alistamento:
  tempo = idade - idade_alistamento
  print("Você já passou em {} anos do tempo do alistamento obrigatório".format(tempo))
