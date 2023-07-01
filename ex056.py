'''
Desenvolva um programa que leia:
Nome, Idade e Sexo de 4 pessoas.
No final do programa, mostre:
A média de idade do grupo;
Qual é o nome do homem mais velho;
Quantas mulheres têm menos de 20 anos.
'''

#Feito na aula:
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p}º PESSOA -----')
    nome = str(input(f'Nome da {p}º pessoa: ')).strip()
    idade = int(input(f'Idade da {p}º pessoa: '))
    sexo = str(input(f'Sexo da {p}º pessoa [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('-' * 30)
print(f'A média do grupo: {mediaidade} anos\n'
      f'Homem mais velho tem {maioridadehomem} anos e se chama: {nomevelho}\n'
      f'Ao todo são {totmulher20} com menos de 20 anos')

print('-' * 30)

#Como eu fiz:

media = 0   #média de idade com base 0
maisv = 0   #idade mais velha
maisn = 0   #idade mais nova
nomev = ''  #nome do mais velho com base vazia

for p in range(1, 5):
    nome = str(input(f'Nome da {p}º pessoa: ')).upper().strip()
    idade = int(input(f'Idade da {p}º pessoa: '))
    sexo = str(input(f'Sexo da {p}º pessoa [M/F]: ')).upper().strip()

    if idade > 1:
        media += idade / 4

    if sexo in 'Mm':
        if idade > maisv:
            maisv = idade
            nomev = nome

    if sexo in 'Ff':
        if idade <= 20:
            maisn += 1
print('-' * 30)
print(f'\033[4;32m{media}\033[m = Média das idades.\n')
print(f'\033[4;34m{nomev}\033[m é o mais homem mais velho, com: \033[4;34m{maisv}\033[m anos.\n')
print(f'\033[4;35m{maisn}\033[m mulheres tem menos de \033[4;35m20\033[m anos.')
