'''
Faça um programa que leia o peso de cinco pessoas.
 No final, mostre qual foi o maior e o menor peso lidos.
'''


maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'{p}º pessoa tem: '))
    if p == 1:      #Se o peso da primeira pessoa for = 1:
        maior = peso    #O maior vai passar a ser o peso
        menor = peso    #E o menor também
    else:   #Se não:
        if peso > maior:    #Se o peso for maior do que o maior:
            maior = peso    #Maior passa a ser o peso
        if peso < menor:
            menor = peso

print(f'Maior peso: {maior}Kg\n'
      f'Menor peso: {menor}Kg')
