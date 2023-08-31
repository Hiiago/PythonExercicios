'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''




lista = []

resp = ''

while resp in 'S':
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Continuar ? [S/N]: ')).upper()
lista.sort(reverse=True)
print('-'*30)
print(f'Foram digitados {len(lista)} números.')

print(f'Lista em forma decrescente: {lista}')

if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('5 não está na lista.')