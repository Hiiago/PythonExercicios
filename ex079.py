'''
Crie um programa onde o usuário possa digitar vários valores numéricos e
 cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
  No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

numeros = list()
resp = ''

while True:
    n = int(input('Digite: '))
    if n not in numeros:
        numeros.append(n)
        print('Adicionado com sucesso...')
    else:
        print('Número já existe.')
    resp = str(input('Continuar ? ')).upper()
    if resp == 'N':
        break

print(f'Programa finalizado. {sorted(numeros)} foram os números digitados.')