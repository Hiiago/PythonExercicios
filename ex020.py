'''O mesmo professor do desafio anterior quer sortear a ordem
de apresentação de trabalhos dos alunos. Faça um programa que
leia o nome dos 4 alunos e mostre a ordem sorteada.'''

import random
a1 = str(input('Nome: '))
a2 = str(input('Nome: '))
a3 = str(input('Nome: '))
a4 = str(input('Nome: '))
print('-' * 35)
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print(f'A ordem para apresentação será:\n'
      f'{alunos}')
