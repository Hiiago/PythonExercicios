'''Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos digitos separados:
1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''

numero = str(input('Um número de 0 a 9999: '))
uni = numero[3]
dez = numero[2]
cen = numero[1]
mil = numero[0]

print(f'O número: {numero}\n'
      f'Para a unidade {uni}\n'
      f'Para a dezena {dez}\n'
      f'Para a centena {cen}\n'
      f'Para o milhar {mil}')
