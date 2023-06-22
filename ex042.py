'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso
 de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

from colorama import Fore, Back, Style
from time import sleep
a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))
if a < b + c and b < a + c and c < a + b:
    print(Fore.LIGHTBLACK_EX + Back.LIGHTCYAN_EX + ('Temos um triângulo... ') + Style.RESET_ALL)
    sleep(1)
    if a == b == c:
        print(Fore.LIGHTBLACK_EX + Back.LIGHTRED_EX + ('EQUILÁTERO')+ Style.RESET_ALL)
    elif a != b != c:
        print(Fore.LIGHTBLACK_EX + Back.LIGHTBLUE_EX + ('ESCALENO')+ Style.RESET_ALL)
    elif a == b != c or b == c != a or c == a != b:         #Poderia usar um else: para evitar escrever tudo
        print(Fore.LIGHTBLACK_EX + Back.LIGHTGREEN_EX + ('ISÓSCELES')+ Style.RESET_ALL)
else:
    print(Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX + ('Não temos um trinângulo ')+ Style.RESET_ALL)
