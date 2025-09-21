import random

aluno1 = input("Digite o seu nome: ")
aluno2 = input("Digite o seu nome: ")
aluno3 = input("Digite o seu nome: ")
aluno4 = input("Digite o seu nome: ")

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista_alunos)

print("A ordem de apresetanção será: {}".format(lista_alunos))