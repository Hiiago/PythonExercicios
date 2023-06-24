'''
Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o
'''

cont = 0
soma = 0
for c in range(1, 7):
    n = int(input('Númbero: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A soma de todos os números páres é de:{soma}\n'
      f'Total de números pares: {cont} ')
