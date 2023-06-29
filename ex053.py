'''
Crie um programa que leia uma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços
exemplo: "apos a sopa", "a sacada da casa" ou "anotaram a data da maratona"
'''

#Ensinado na aula
frase = str(input('Uma frase: ')).upper().strip()

palavras = frase.split()        #Gerando uma lista
junto = ''.join(palavras)       #Juntando essa lista em uma string para elimidar os espaços
inverso = ''
for letra in range(len(junto) - 1, -1, -1):  #O inverso dela. Da última letra, até a primeira, voltando uma letra
    inverso += junto[letra]
if inverso == junto:        #Se inverso está dentro do junto
    print('\033[32mTemos um palíndromo\033[m !')
else:
    print('\033[31mNão temos um palíndromo !\033[m')
print(f'\033[34mO inverso de {junto} = {inverso}')

#Como eu fiz
join = (''.join(frase.split()))
palin = frase = join
if frase[::-1] in join:
    print('\033[32mTemos um palíndromo !\033[m')
else:
    print('\033[31mNão temos um palíndromo !\033[m')
print(f'\033[34m{frase} = {palin[::-1]}')
