'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e
 cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
  No final, mostre a lista ordenada na tela.
'''


lista = list()

for c in range(0, 5):
    n = int(input(f'Digite o {c}º valor: '))
    if c == 0 or n > lista[-1]: #Se o c for igual a 0, primeiro ou o for maior que o ultimo valor:
        lista.append(n) #Ele é adicionado no final da lista
        print('Adicionado ao final da lista.')
    else:   # Se não
        pos = 0
        while pos < len(lista): #da posição 0 até a ultima
            if n <= lista[pos]: #Se o n é menor ou igual a ele
                lista.insert(pos, n) #Insere o valor na posição listada
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1 #Para ir passando pra proxima posição
print('='*30)
print(f'Valores em ordem foram: {lista}')
