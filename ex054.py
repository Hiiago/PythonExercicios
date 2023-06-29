'''
Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade
  e quantas já são maiores.
'''

from datetime import date
atual = date.today().year
maiori = 0
meno = 0
for p in range(1, 8):
    nasci = int(input(f'Em que ano a {p}º pessoa nasceu ? '))
    idade = atual - nasci
    if idade >= 21:
        maiori += 1
    else:
        meno += 1
print('-' * 30)
print(f'\033[31m{maiori}\033[m <= Atingiram a maioridade\n'
      f'\033[31m{meno}\033[m <= Não atingiriam maioridade ')
