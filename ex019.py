'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos
e escrevendo na tela o nome do escolhido.'''


from random import choice
aluno1 = str(input('Nome: '))
aluno2 = str(input('Nome: '))
aluno3 = str(input('Nome: '))
aluno4 = str(input('Nome: '))
alunos = (aluno1, aluno2, aluno3, aluno4)
print('-' * 35)
escolhido = choice(alunos)
print(f'O aluno escolhido foi: {escolhido}')
