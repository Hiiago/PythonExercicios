'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número
 entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
  mostrando no final quantos palpites foram necessários para vencer.
'''

#Feito na aula:
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabeei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi ? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite ?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print(f'Acertou em {palpites} tentativas, parabéns! ')

print('-' * 50)
#Como eu fiz:
from random import randint
from time import sleep
print('COMPUTADOR: Pensei num número entre 0 e 10 tente advinhar !')
print('-'*30)
numero = int(input('Número: '))
print('-'*30)
sleep(1)
computador = randint(0, 10)   #Numero aleatorio entre 0 - 5
cont = 0
while numero != computador:
    cont += 1
    if computador > numero:
        print('Mais...')
    else:
        print('Menos...')
    numero = int(input('Tente novamente: '))
else:
    print('Ganhou! ')
print(f'\033[34mO número escolhido foi \033[4;7;35m{computador}\033[m\n'
      f'\033[33mTotal de tentativas: \033[4;7;36m{cont}\033[m')
