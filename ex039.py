'''Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
  se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
tempo = 18 - idade

if idade == 18:
    print(f'Você já está com {18} anos, hora de se alistar no exército! ')
elif idade < 18:
    print(f'Você está com {idade} anos, não está na hora de se alistar.')
    print(f'Ainda faltam {tempo} ano(s) para seu alistamento.')
elif idade > 18:
    print(f'Já passou do tempo de alistamento, você tem {idade} anos ')
    print(f'Já passou {tempo} ano(s) do seu alistamento.')
