'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from colorama import Fore
from random import randint
print(Fore.CYAN + ('[ 0 ] PEDRA'
      '[ 1 ] PAPEL'
      '[ 2 ] TESOURA'))
jogador = int(input(Fore.YELLOW + ('Qual é sua jogada ? ')))
maquina = randint(0, 3)
jogadorg = jogador == 0 and maquina == 2 or jogador == 1 and maquina == 0 or jogador == 2 and maquina == 1

if jogador == maquina:
    print(Fore.BLUE + ('DEU EMPATE'))
elif jogador == jogadorg:
    print(Fore.GREEN + ('Você Ganhou !'))
else:
    print(Fore.RED + ('Você perdeu'))
print(Fore.LIGHTWHITE_EX + (f'Você escolheu: {jogador}\nMáquina escolheu: {maquina}'))
