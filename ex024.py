''' Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".'''

cidade = str(input('Cidade: ')).strip()
print('SANTO' in cidade[:5].upper())
print(cidade)

cidade = str(input('Cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
print(cidade)
