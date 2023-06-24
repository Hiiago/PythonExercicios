'''
Refaça o DESAFIO 009, mostrando a tabuada de
um número que o usuário escolher, só que agora utilizando um laço for.
'''

'''
num = int(input('Digite um numero para ver sua tabuada: '))
print('-'*20)
print(f'{num} * {1} = {num*1}\n'
        f'{num} * {2} = {num*2}\n'
        f'{num} * {3} = {num*3}\n'
        f'{num} * {4} = {num*4}\n'
        f'{num} * {5} = {num*5}\n'
        f'{num} * {6} = {num*6}\n'
        f'{num} * {7} = {num*7}\n'
        f'{num} * {8} = {num*8}\n'
        f'{num} * {9} = {num*9}\n'
        f'{num} * {10} = {num*10}')
print('-'*20)
'''
print('-'*30)
n = int(input('Um número para sua tabuada: '))
for c in range(1, 11):
    print(f'{c} x {n} = {c * n}')
print('-'*30)
