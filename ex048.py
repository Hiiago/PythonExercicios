'''Faça um programa que calcule a soma entre
todos os números que são múltiplos de três e
que se encontram no intervalo de 1 até 500.'''

s = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:          #Vendo se número é impar e multiplo de 3
        s = s + i           #Soma = Soma + o range (todos numeros multiplos de 3 que são impar)
        cont = cont + 1     #Contagem = contagem + 1
print(f'Soma de todos os {cont} valores é = {s}', end=' ')

soma = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:       #Vendo se número é impar e multiplo de 3
        soma += c       #Soma = Soma + o range (todos numeros multiplos de 3 que são impar)
print(f'\nSoma de todos os valores é = {soma}')
