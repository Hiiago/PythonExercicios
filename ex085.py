'''
Crie um programa onde o usuário possa digitar sete valores numéricos
 e cadastre-os em uma lista única que mantenha separados os valores
  pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

# Como fiz:
num = []
par = []
impar = []

for n in range(1, 8):
    num.append(int(input(f'{n}º Valor: ')))
    if n % 2 == 0:
        par.insert(0, n)
        num.pop()
    if n % 2 != 0:
        impar.insert(0, n)
        num.clear()
print('-='*30)
print(f'Os valores pares digitados foram: {sorted(par)}')
print(f'Os valores impares digitados foram: {sorted(impar)}')


#Feito na aula:
num = [[], []]

for n in range(1, 8):
    valor = int(input(f'{n}º Valor: '))
    if n % 2 == 0:
        num[0].append(valor)  #Na chave [0] de num adicione o valor par
    else:
        num[1].append(valor)  #Na chave [1] de num adicione o valor impar
print('-='*20)
print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores impares digitados foram: {sorted(num[1])}')
