# Criar programa que leia quanto de dinheiro uma pessoa tem na carteira
# e mostrar quantos dólares ela pode comprar.
# ex: US$1,00 = R$4,81

carteira = float(input('Dinheiro na carteira: US$'))
real = 4.81
conversor = carteira * real
print(f'Se na carteira eu tenho {carteira}, então em real eu tenho {conversor:.2f}')
