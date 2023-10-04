'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep

lista = [] #lista temporária
jogos = [] #lista que usaremos
print('-'*35)
print('-=-=-=-   JOGA NA MEGA SEGA   -=-=-=-')
print('-'*30)
quant = int(input('Quantos jogos quer que eu sorteie ? '))
cont = 0 #Contador
tot = 1 #Total
while tot <= quant: #Enquanto total for menor que a quantidade
    cont = 0 #Contador recebe 0
    while True: #Enquanto for verdadeiro
        num = randint(1, 60) #Numeros que serão randomizados
        if num not in lista: #Se numero nao estiver na lista
            lista.append(num) #Coloque na lista
            cont += 1 #Contador recebe mais um
        if cont >= 6: #Se o contador for maior ou igual a 6:
            break #Pare o programa
    lista.sort() #Colocando a lista em ordem
    jogos.append(lista[:]) #Copiando a lista temporária para o jogos
    lista.clear() #Apagando a lista temporária
    tot += 1 #Total + 1
print('-=-'*3, f'SORTEANDO {quant} JOGOS', '-=-'*3)
for i, l in enumerate(jogos): #Para cada indice da lista em numeração:
    print(f'Jogo {i+1}: {l}')  #mostrando o numero do jogo e os número sorteador.
    sleep(1) #Pausa para mostrar o print.
