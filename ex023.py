'''Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos digitos separados:
1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''

numero = int(input('Numero de 0 a 9999: '))

uni = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10

print(f'Unidade: {uni}\n'
      f'Dezena: {dez}\n'
      f'Centena: {cen}\n'
      f'Milhar: {mil}')

'''a cada 10 unidades, formamos 1 dezena (10 unidades); 
a cada 10 dezenas, formamos 1 centena (100 unidades); 
a cada 10 centenas, formamos 1 unidade de milhar (1.000 unidades). 
Sempre que o algarismo 0 é acrescentado, devemos multiplicar a ordem por 10.'''
#divisão inteira e depois o resto da divisão
#o símbolo // faz a divisão e só pega o que esta antes da vírgula.
#o símbolo % faz a divisão e só pega o que esta depois da vírgula.