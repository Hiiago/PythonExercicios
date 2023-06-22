'''
Elabore um programa que calcule o valor a ser pago por um produto,
 considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
from colorama import Fore
print(Fore.LIGHTRED_EX + ('Bem Vindo a SuperChoque ! '))
print('-' * 50)
mouse = float(input(Fore.LIGHTCYAN_EX + ('Preço do mouse: ')))
print('-' * 50)
print(Fore.LIGHTGREEN_EX + ('[ 1 ] dinheiro/pix: 10% desconto\n'
      '[ 2 ] débito: 5% de desconto\n'
      '[ 3 ] crédito 2x\n'
      '[ 4 ] crédito 3x ou mais: 20% de juros '))
paga = int(input(Fore.LIGHTWHITE_EX + ('Forma de pagamento: ')))
print('-' * 50)
if paga == 1:
    a = mouse - (mouse * 10) / 100
    print(Fore.BLACK + (f'10% de deconto no valor de {mouse}\nValor a pagar via dinheiro/pix: R${a}'))
elif paga == 2:
    b = mouse - (mouse * 5) / 100
    print(Fore.CYAN + (f'5% de desconto no valor de {mouse}\nValor a pagar via débito: R${b}'))
elif paga == 3:
    print(Fore.LIGHTMAGENTA_EX + (f'2x no cartão de crédito\nPreço a pagar via cartão de crédito: R${mouse}'))
elif paga == 4:
    c = mouse + (mouse * 20) / 100
    print(Fore.LIGHTYELLOW_EX + (f'3x ou mais no cartão de crédito no valor de {mouse}\nValor a pagar com 20% de juros: R${c}'))
print('-' * 50)
print(Fore.LIGHTRED_EX + ('          Foi um prazer recebê - lo! '))
