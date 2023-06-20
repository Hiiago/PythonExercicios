'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.'''

km = float(input('Qual a distância da viagem em km/h ? '))
passagem = km * 0.50
passagem2 = km * 0.45
print(f'Você viajará por {km:.2f}km.')
if km < 200:
    print(f'O preço da passagem ficou em R${passagem:.2f} reais')
else:
    print(f'O preço da passagem ficou em R${passagem2:.2f} reais')
