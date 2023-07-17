'''
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''


#Feito na aula:

while True:
    n = int(input('Quer ver a tabuada de qual valor ? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADA. VOLTE SEMPRE !')



#Como eu fiz:
num = int(input('Número: '))
print('-'*20)
cont = 0
while True:
    if num < 0:
        break
    while cont < 10:
        cont += 1
        print(f'{num} x {cont} = {cont * num}')
        if cont == 10:
            cont -= cont
            print('-' * 20)
            num = int(input('Número: '))
            if num < 0:
                break
            cont += 1
            print(f'{num} x {cont} = {cont * num}')
print('Tabuada finalizada. Volte sempre!')
