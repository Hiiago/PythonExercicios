'''Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa'''

from math import hypot
a = float(input('comprimento do cateto oposto: '))
b = float(input('compirmento do cateto adjacente: '))
print('-' * 45)
print(f'RESOLUÃO\n'
      f'Comprimento: {a}m\n'
      f'Largura: {b}m')
print(f'O comprimento da hipotenusa é de: {hypot(a, b):.2f}m')
print('-' * 45)