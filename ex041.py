'''A Confederação Nacional de Natação precisa de um programa que leia
 o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from colorama import Fore
from datetime import date
atual = date.today().year
nasci = int(input(Fore.LIGHTMAGENTA_EX + ('Ano de nascimento: ')))

idade = atual - nasci

if idade <= 9:
    print(Fore.YELLOW + (f'{idade} anos = MIRIM'))
elif idade <= 14:
    print(Fore.LIGHTWHITE_EX + (f'{idade} anos = INFANTIL'))
elif idade <= 19:
    print(Fore.GREEN + (f'{idade} anos = JÚNIOR'))
elif idade <= 25:
    print(Fore.BLUE + (f'{idade} anos = SÊNIOR'))
else:
    print(Fore.LIGHTWHITE_EX + (f'{idade} anos = MASTER'))
