'''
 Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e
 qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não
 continuar a digitar valores.
'''


n = cont = soma = maior = menor = 0
resp = 'S'

while resp == 'S':
    n = int(input('Número: '))
    resp = str(input('Continuar ? ')).upper().strip()[0]
    cont += 1
    soma += n

    if cont == 1:       #Se a quantidade de valor digitados é = 1, então o maior e o menor são 1
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / cont
print('-' * 30)
print(f'{cont} = TOTAL\n'
      f'{media:.2f} = MÉDIA\n'
      f'{maior} = MAIOR\n'
      f'{menor} = MENOR')
