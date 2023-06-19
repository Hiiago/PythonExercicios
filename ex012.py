'''ler o preço de um produto
    e mostrar o novo preço com 5% de desconto'''

PcGamer = float(input('Quantos quer pelo Pc Gamer: R$'))
desconto = PcGamer - (PcGamer * 60 / 100)
print(f'O valor do pc está em {PcGamer}\n'
      f'Adicionei 5% de desconto, ficando: {desconto}')
