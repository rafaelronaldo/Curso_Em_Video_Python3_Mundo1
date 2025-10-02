nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1+nota2)/2
if media < 5:
  print("Sua média é de {} e você está \033[31mREPROVADO!\033[m".format(media))
elif media >=5 and media <= 6.9:
  print("Sua média é de {} e você está em \033[33mRECUPERAÇÃO!\033[m".format(media))
else:
  print("Sua média é de {} e você está \033[32mAPROVADO!\033[m".format(media))