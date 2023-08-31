'''
Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''


lista = []
pares = []
impares = []
resp = ''


while resp in 'S':
    num = int(input('Digite um valor: '))
    resp = str(input('Continuar ? [S/N]: ')).upper()
    if num % 2 == 0:
        lista.append(num)
        pares.append(num)
    else:
        lista.append(num)
        impares.append(num)
print('-'*30)
print(f'{lista}\n'
      f'{pares}\n'
      f'{impares}')
