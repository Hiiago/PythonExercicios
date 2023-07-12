'''
Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999,
  que é a condição de parada.
   No final, mostre quantos números foram digitados e
    qual foi a soma entre eles (desconsiderando o flag).
'''

#Como eu fiz:

n = tot = soma = 0
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    if n != 999:
        tot += 1
        soma += n
print(f'O total de números digitados foram: {tot}\n'
      f'E a soma total foi de: {soma}')

#Na aula:

n = tot = soma = 0
n = int(input('Digite um valor [999 para parar]: '))
while n != 999:
    soma += n
    tot += 1
    n = int(input('Digite um valor [999 para parar]: '))
print(f'O total de números digitados foram: {tot}\n'
      f'E a soma total foi de: {soma}')
