'''
Desenvolva um programa que leia o primeiro
 termo e a razão de uma PA. No final, mostre
  os 10 primeiros termos dessa progressão.
'''


ini = int(input('Inicio: '))    #Primeiro termo (primeiro número)
raz = int(input('Razão: '))     #Razão (número que pula)
for c in range(1, 11):          #(1, 10 = 10 primeros termos)
    term10 = ini + (c - 1) * raz    #Calculo para mostrar os 10 primeiros termos
    print(f'{term10} ', end=' > ')
print(f'ACABOU'
      f'\nPrimeiro termo: {ini}\n'
      f'Razão: {raz}')

prim = int(input('Inicio: '))
razao = int(input('Razão: '))
decimo = prim + (10 - 1) * razao
for c in range(prim, decimo + razao, razao):
    print(f'{c}', end=' > ')
print('ACABOU')