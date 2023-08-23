'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
 Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

import random


maior = 0
menor = 0


print('Os números sorteados foram: ', end='')
for c in range(0, 5):
    numeros = (random.randint(0, 10))
    print(f'{numeros}', end=' ')


