'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
'''

valorca = float(input('Valor da casa: R$'))
salarioco = float(input('Salário do comprador: R$'))
qtsanos = int(input('Quantos anos de pagamento: '))
print('-'*50)

parcela = (valorca / qtsanos) / 12
emprestimo = (salarioco * 30) / 100

print(f'Para pagar uma casa de R${valorca:.2f} em {qtsanos} anos, a prestação será de R${parcela:.2f}.')
if parcela > emprestimo:
    print('O valor da parcela excedeu 30% do salário do comprador. Empréstimo negado')
elif parcela < emprestimo:
    print('Empréstimo Aceito!')
print(f'Empréstimo {emprestimo:.2f}')
