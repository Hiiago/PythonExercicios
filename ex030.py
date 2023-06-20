'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

from colorama import Fore

numero = int(input('Um número: '))
if numero % 2 == 0:
    print(Fore.RED + f'{numero} é PAR!')
else:
    print(Fore.BLUE + f'{numero} é ÍMPAR!')
