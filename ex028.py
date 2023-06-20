'''Jogo da advinhação
 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
 tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
print('COMPUTADOR: Pensei num número entre 0 - 5 tente advinhar !')
print('-'*30)
numero = int(input('Número: '))
print('-'*30)
sleep(1)
computador = randint(0, 5)   #Numero aleatorio entre 0 - 5
if numero == computador:
    print('Parabéns, acertou!! ')
else:
    print('Número errado! ')
print(f'O número pensado foi {computador}!!')
