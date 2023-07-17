'''
Crie um programa que leia números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999,
  que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''


total = soma = 0
while True:
    num = int(input('Números: '))
    if num == 999:
        break
    total += 1
    soma += num
print(f'\033[35m{total}\033[m = Total de números digitados.\n'
      f'\033[34m{soma}\033[m = Soma entre todos os números.')
