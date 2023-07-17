'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder.
No final mostre o total de vitórias consecutivas
que conquistou no jogo.
'''


#Feito na aula:
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes.')

#Meu jeito:

from random import randint
print('=' * 40)
print('- ! VAMOS JOGAR PAR OU ÍMPAR ! -')
print('=' * 40)

opcao = ''
cont = 0

while True:
    computador = randint(1, 9)
    pessoa = int(input('Qual valor ? '))
    escolha = str(input('Par ou ímapar? ')).upper().split()[0]
    total = pessoa + computador
    print('-' * 40)

    if total % 2 == 0:
        opcao = 'PAR'
    if total % 2 != 0:
        opcao = 'IMPAR'

    print(f'Você jogou {pessoa} e o computador {computador}. Total de {total}, deu {opcao}')
    print('-' * 40)
    if escolha == opcao:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
        break
    cont += 1
    print('=' * 40)
print(f'GAME OVER ! Você venceu {cont} vezes.')
