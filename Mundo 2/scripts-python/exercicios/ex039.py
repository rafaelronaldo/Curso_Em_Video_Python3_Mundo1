from datetime import date
atual = date.today().year
ano_nasc = int(input("Digite o seu ano de nascimento: "))
idade = atual - ano_nasc
idade_alistamento = 18
print("Quem nasceu em {} tem {} anos em {}".format(ano_nasc, idade, atual))
if idade < idade_alistamento:
  tempo = idade_alistamento - idade
  print("Ainda faltam {} anos para o alistamento.".format(tempo))
elif idade == idade_alistamento:
  print("Você tem que se alistar \033[32mIMEDIATAMENTE!\033[m")
else:
  tempo = idade - idade_alistamento
  ano_de_alistamento = atual - tempo
  print("Você já deveria ter se alistado há {} ano(s)".format(tempo))
  print("Seu alistamento foi em {}".format(ano_de_alistamento))