'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

#Feito na aula
print('+-=' * 16)
print('GERADOR DE PA')
print('+-=' * 16)
prim = int(input('Inicio: '))
razao = int(input('Razão: '))
termo = prim
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo += razao
    cont += 1
print('FIM')


#Como eu fiz:
print('+-=' * 16)
print('GERADOR DE PA')
print('+-=' * 16)
prim = int(input('Inicio: '))
razao = int(input('Razão: '))
decimo = prim + (10 - 1) * razao
while prim < decimo + razao:
    print(f'{prim}', end=' > ')
    prim += razao
print('FIM')
