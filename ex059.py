'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
a = int(input('\033[7;36mPrimeiro valor:\033[m '))
b = int(input('\033[7;36mSegundo valor:\033[m '))
print('\033[1;97m-' * 30)

print('\033[7;35;40m[ 1 ] SOMAR\n'
      '[ 2 ] MULTIPLICAR\n'
      '[ 3 ] MAIOR VALOR\n'
      '[ 4 ] NOVOS NÚMEROS\n'
      '[ 5 ] SAIR DO PROGRAMA\033[m')
c = ''
while c != 5:
    c = int(input('\033[7;34mSelecione Uma Opção:\033[m '))
    print('\033[1;97m-' * 30)

    if c == 1:
        print(f'\033[4;31mA soma dos valores: {a} + {b} = {a + b}')
    elif c == 2:
        print(f'\033[4;32mA multiplicação dos valores: {a} * {b} = {a * b}')
    elif c == 3:
        print(f'\033[4;33mO maior valor entre {a} e {b} é = {max(a, b)}')
    elif c == 4:
        a = int(input('\033[7;36mPrimeiro valor:\033[m '))
        b = int(input('\033[7;36mSegundo valor:\033[m '))
        print('\033[7;35;40m[ 1 ] SOMAR\n'
              '[ 2 ] MULTIPLICAR\n'
              '[ 3 ] MAIOR VALOR\n'
              '[ 4 ] NOVOS NÚMEROS\n'
              '[ 5 ] SAIR DO PROGRAMA\033[m')
    if c == 5:
        print('\033[1;36mSaindo do programa...')

