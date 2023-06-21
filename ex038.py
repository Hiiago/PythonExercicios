''' Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

a = int(input('Número inteiro: '))
b = int(input('Número inteiro: '))

if a > b:
    print(f'\033[4;32mA é o maior ! {a}\033[m ')
elif b > a:
    print(f'\033[4;34mB é maior ! {b}\033[m ')
elif a == b:
    print(f'\033[4;31mA e B tem o mesmo valor !{a}\033[m ')

