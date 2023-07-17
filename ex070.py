'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

#Feito na aula:
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'R${total:.2f} = Total dos produtos.\n'
      f'{totmil} = Produtos custam mais de R$1.000,00.\n'
      f'{barato} = Nome do produto mais barato, que custa {menor}')


#Como eu fiz:
print('     ¹²³')
print('Games e Jogos')
print('-' * 25)

total = 0
resp = ''
mais1000 = 0
barato = 0
nomeba = ''
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$'))
    if valor > 0:
        total += valor
    if valor >= 1000:
        mais1000 += 1
    if nomeba == '' or valor < barato:      #Isso adicionará um nome ao produto mais barato se nomeba não estiver valor
        barato = valor                      # e se o valor for menor que barato
        nomeba = nome
    resp = str(input('Continuar compra ? ')).strip().upper()[0]
    if resp == 'N':
        break
print('=' * 35)
print(f'R${total:.2f} = Total dos produtos.\n'
      f'{mais1000} = Produtos custam mais de R$1.000,00.\n'
      f'{nomeba} = Nome do produto mais barato, que custa {barato}')
