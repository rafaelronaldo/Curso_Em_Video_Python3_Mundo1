nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1+nota2) / 2
print("Tirando {} e {}, a média do aluno é {}".format(nota1, nota2, media))
if media < 5:
  print("O aluno está \033[31mREPROVADO\033[m")
elif media >= 5 and media <= 6.9:
  print("O aluno está em \033[33mRECUPERAÇÃO\033[m")
else:
  print("O aluno está \033[32mAPROVADO\033[m")

