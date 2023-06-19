'''Crie um programa que leie um número real qualquer
e mostre sua porção inteira'''

from math import trunc
num = float(input('Numero real: '))
print(f'{trunc(num)}')
