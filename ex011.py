'''ler a largura e altura de uma parede em metros
    calcular sua área e a quantidade de tinta
    necessária para pintá-la
    sabendo que cada litro, pinta uma área de 2m².
'''

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura * largura
tinta = area / 2
print(f'Temos a área de: {area:.2f}m²\n'
      f'A quantidade de litros de tinta necessária será: {tinta:.2f}l')
