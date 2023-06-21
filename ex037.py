'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
 1 para binário,
  2 para octal e
   3 para hexadecimal.
'''

from time import sleep
from colorama import Fore, Back, Style

n = int(input(Fore.LIGHTGREEN_EX + ('Número inteiro: ')))
print(Back.LIGHTMAGENTA_EX + Fore.BLACK + ('''ESCOLHA UMA DAS BASES PARA CONVERSÃO:
[1] BINÁRIO [2] OCTAL [3] HEXADECIMAL''') + Style.RESET_ALL)
print('-' * 100)
num = int(input(Fore.LIGHTGREEN_EX + ('Sua opção: ')))
print('-' * 100)
sleep(1)
if num == 1:
    print(Fore.BLUE + (f'A conversão do número inteiro {n} para BINÁRIO é = {bin(n)[2:]}'))
elif num == 2:
    print(Fore.GREEN + (f'A conversão do número inteiro {n} para BINÁRIO é = {oct(n)[2:]}'))
elif num == 3:
    print(Fore.YELLOW + (f'A conversão do número inteiro {n} para BINÁRIO é = {hex(n)[2:]}'))
else:
    print(Fore.RED + ('DIGITO INVÁLIDO'))

'''EXPLICANDO
[2:] Para tirar os dois primeiros digitos quando converte
import colorama: Biblioteca das cores 
import sleep: Para ter uma pausa de (1) segundo no terminal
'''
