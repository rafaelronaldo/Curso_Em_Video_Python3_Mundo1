import random

aluno1 = input("Digite o seu nome: ")
aluno2 = input("Digite o seu nome: ")
aluno3 = input("Digite o seu nome: ")
aluno4 = input("Digite o seu nome: ")

lista_alunos = aluno1, aluno2, aluno3, aluno4

aluno_sorteado = random.choice(lista_alunos)

print("Aluno sorteado: {}".format(aluno_sorteado))