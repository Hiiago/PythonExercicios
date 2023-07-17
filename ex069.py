'''
Crie um programa que leie a idade e sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar.
No final mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''

mais18 = homens = mulh20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            mulh20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{mais18} = Total de pessoas com mais de 18 anos.\n'
      f'{homens} = Total de homens cadastrados.\n'
      f'{mulh20} = Total de mulheres com menos de 20 anos.')
