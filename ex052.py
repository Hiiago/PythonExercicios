'''Faça um programa que leia um número
 inteiro e diga se ele é ou não um número primo.'''

'''numero = int(input('Número inteiro: '))
if numero % numero == 1 and numero % 1 == numero:
    print(f'O número {numero} foi divisível 2 vezes ')
else:
    print(f'{numero} não é primo! ')'''

numero = int(input('\033[34mNúmero inteiro: '))
total = 0   #Total de divisões feitas nesse numero inteiro
for c in range(1, numero+1):    #Do 1 ao "numero" digitado
    if numero % c == 0:     #Calculando quantos numeros tem resto 0
        print(f'\033[33m', end=' ')     #Colocando cor vermelha em numeros nao divisiveis
        total += 1  #Adicionando mais um onde tem - se mais de um numero de divisão
    else:
        print(f'\033[31m', end=' ')     #Cor amarela para numeros divisiveis
    print(f'{c}', end=' ')      #Mostrando no terminal os numeros identificados
print(f'\n\033[36mO número {numero} foi divisivel {total} vezes.')
if total == 2:  #Se o total de numeros divisiveis for igual a 2: print(é numero primo)
    print('\033[32mE por isso ele é PRIMO!')
else:           #E o se não é o contrário do if
    print('\033[35mE por isso ele NÃO É PRIMO!')


