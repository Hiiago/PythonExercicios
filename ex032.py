''' Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''

'''ano = int(input('Ano: '))
if ano % 4 == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é bissexto')
'''

from datetime import date
ano = int(input('Que ano quer listar ?\n'
                'Coloque 0 para analisar o ano atual: '))
print('-' * 30)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é bissexto!')


#um ano é bissexto se for divisível por 4, exceto quando também é divisível por 100.
#No entanto, os anos que são divisíveis por 400 são considerados bissextos novamente.