'''Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''


# Recebendo informação de salario
salario = float(input('Salário atual: '))

# Fazendo analise e calculando aumento
if salario > 1250:
    aumento = salario + (salario * 10) / 100
    print(f'Salário de R${salario:.2f} aumentou em 10%: R${aumento}')
else:
    outro = salario + (salario * 15) / 100
    print(f'Salário de R${salario:.2f} aumentou em 15%: R${outro}')
