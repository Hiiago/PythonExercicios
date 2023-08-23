'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileirode Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Corinthians.
'''


tabela = ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras' , 'Bragantino',
          'Grêmio', 'Athletico-PR', 'Cuiabá', 'São Paulo', 'Atlético-MG',
          'Cruzeiro', 'Internacional', 'Fortaleza', 'Corinthians', 'Goiás',
          'Bahia', 'Santos', 'Coritiba', 'Vasco', 'América-MG')
tabela2 = tabela
print('Os 5 primeiros times são: ')
for cont in range(0, len(tabela[:5])):
    print(f'{tabela[cont]}')
print('-'*30)

print('Os últimos 4 times são: ')
for cont in range(16, len(tabela[:20])):
    print(f'{tabela[cont]}')
print('-'*30)

print('Tabela em ordem alfabetica: ')
print(f'{sorted(tabela)}')
print('-'*30)

print(f'Corinthians está na {tabela2.index("Corinthians")+1}ª posição')
