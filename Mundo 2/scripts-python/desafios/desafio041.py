ano_nasc = int(input("Digite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nasc

if idade <= 9:
  print ("Você tem {} de idade e está na categoria \033[31mMIRIM!\033[m".format(idade))
elif idade <= 14:
  print("Você tem {} de idade e está na categoria \033[32mINFANTIL!\033[m".format(idade))
elif idade <= 19:
  print("Você tem {} de idade e está na categoria \033[33mJUNIOR!\033[m".format(idade))
elif idade <= 20:
  print("Você tem {} de idade e está na categoria \033[34mSÊNIOR!\033[m".format(idade))
else:
  print("Você tem {} de idade e está na categoria \033[35mMASTER!\033[m".format(idade))