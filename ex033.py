'''Faça um programa que leia 3 números e mostre:
o maior e o menor.'''

# 3 números fornecidos pelo usuário
print('Me dê 3 números: ')
a = int(input('A) '))
b = int(input('B) '))
c = int(input('C) '))

# Inicialização das variáveis (consideramos que "a" é o menor e menor para inicio da comparação)
maior = a
menor = a

# Verificando qual o maior e menor número
# Comparação com o segundo número
if b > maior:
    maior = b
elif b < menor:
    menor = b
# Comparação com o terceiro número
if c > maior:
    maior = c
elif c < menor:
    menor = c

# Resultado
print(f'Maior = {maior}')
print(f'Menor = {menor}')

#Outra forma de fazer sem if
print('-' * 20)
print('Me dê 3 números: ')
a = int(input('A) '))
b = int(input('B) '))
c = int(input('C) '))

maior = max(a, b, c)    #Valor máximo
menor = min(a, b, c)    #Valor mínimo

print(f'Maior = {maior}')
print(f'Menor = {menor}')
