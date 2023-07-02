'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

#Feito na aula
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')


#Como eu fiz:
from math import factorial

num = int(input('Número para fatorar!: '))
c = num
print(f'O fatorial de {num}! = ', end='')
while c > 0:   #Enquanto o contador (c) for menor do que 10:
    print(f'{c}', end=' x ')
    c -= 1
print(f'= {factorial(num)}')
