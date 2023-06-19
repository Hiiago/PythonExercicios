'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km = float(input('Quantos km rodou ? '))
dia = int(input('Quantos dias alugou ? '))
diaria = 60 * dia
kms = 0.15 * km
total = diaria + kms
print(f'Km percorrido: {km}km\n'
      f'Dias alugados: {dia} dias\n'
      f'A diária foi de R${diaria:.2f}\n'
      f'Kms foi de {kms:.2f}km\n'
      f'Total a pagar: R${total:.2f}')
