''' Ler o salário de um funcionário
    e mostrar seu novo salário com aumento de 15%'''

salario = float(input('Meu salário: R$'))
aumento = salario + (salario * 15 / 100)
print(f'Meu salário era de: {salario}\n'
      f'Com aumento ficou {aumento}')
