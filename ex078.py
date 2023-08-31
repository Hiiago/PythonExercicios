'''
Faça um programa que leia 5 valores numéricos e guarde-os numa lista.
 No final, mostre qual foi o maior e o menor valor digitado
  e as suas respectivas posições na lista.
'''

numeros = list()
maior = 0
menor = 0

for i in range(0, 5):
    numeros.append(int(input(f'Digite o valor na posição {i}: ')))
    if i == 0:
        maior = menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
print('='*30)
print(f'Os numeros digitados foram: {numeros}')
print(f'Maior: {maior} nas posições ', end='')
for c, v in enumerate(numeros):
    if v == maior:
        print(f'{c}... ', end='')
print(f'\nMenor: {menor} nas posições ', end='')
for c, v in enumerate(numeros):
    if v == menor:
        print(f'{c}... ', end='')
print()
