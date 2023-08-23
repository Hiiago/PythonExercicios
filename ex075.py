'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
 No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''


a = (int(input('Primeiro valor: ')))
b = (int(input('Segundo valor: ')))
c = (int(input('Terceiro valor: ')))
d = (int(input('Quarto valor: ')))

tupla = (1, a, b, c, d)       #A vírgula é usada para colocar os valores em uma tupla

cont = 0


print('='*20)
print(f'Os valores digitados foram ({a}, {b}, {c}, {d})')
print(f'O valor 9 aparece: {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 está na {tupla.index(3)}ª posição')
else:
    print('Valor 3 não foi digitado')

print(f'Os números pares digitados foram:', end=' ')

if a % 2 == 0:
    cont += 1
    print(f'{a}', end=' ')
if b % 2 == 0:
    cont += 1
    print(f'{b}', end=' ')
if c % 2 == 0:
    cont += 1
    print(f'{c}', end=' ')
if d % 2 == 0:
    cont += 1
    print(f'{d}', end=' ')

