'''
Crie um programa que tenha uma dupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'trêze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

resp = ' '
while True: #enquanto for verdade:
    pessoa = int(input('Digite um número entre 0 e 20: '))  #Peça para digitar um número.
    if 0 <= pessoa <= 20:   #Se o número estiver entre 0 e 20:
        break   #O programa vai parar .
    print('Tente novamente. ', end='')  #Se o número não estiver entre 0 e 20, será pedido novamente.
print(f'Você digitou o número: {(numeros[pessoa])}')    #Se o número digitado estiver entre 0 e 20, irá mostrar o número.
