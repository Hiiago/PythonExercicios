'''
Crie um programa que tenha uma tupla única com nomes de produtos e
 seus respectivos preços, na sequência. No final, mostre uma listagem
  de preços, organizando os dados em forma tabular.
'''

itens = ('mouse', 50, 'teclado', 150, 'monitor', 850, 'headset', 300,
         'cooler', 250, 'processador', 900, 'placa de vídeo', 2500,
         'fans rgb', 120, 'memória ram', 200, 'ssd', 250, 'nvme', 350)

print('-' * 50)
print('                  finslan tech')
print('-' * 50)

for i in range(0, len(itens), 2):
    print(f'{itens[i]:.<8}..............................R$ {itens[i+1]:>5.2f}')

print('-' * 50)
