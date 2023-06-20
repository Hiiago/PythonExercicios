'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

from colorama import init, Fore, Back, Style

km = int(input('Kms/h: '))
limite = 80
multa = (km - limite) * 7
if km > 80:
    print(Fore.RED + (f'Você ultrapassou o limite, terá que pagar R${multa} de multa!! '))
else:
    print(Back.GREEN + 'Velocidade na média permitida!')
print(Back.LIGHTBLACK_EX + '-' * 50)
print(Style.BRIGHT + 'Tenha um bom dia!')

