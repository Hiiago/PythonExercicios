'''
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
 No final, mostre a matriz na tela, com a formatação correta.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  #Lista com 3 listas dentro com 3 valores em cada lista (para nao usar append) para depois substituir os 0 por valores
#For de alimentação. o que vou colocar os valores dentro da matriz
for l in range(0, 3):   #laço de linhas
    for c in range(0, 3):   #Laço de colunas
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) #esses valores vão para cada linha e coluna indicadas

print('=='*30)  #dividindo linha

#For para mostrar a estrutura na tela
for l in range(0, 3): #Laço de linhas
    for c in range(0, 3): #laço de colunas
        print(f'[{matriz[l][c]:^5}] ', end='')  #Mostrando os valores em ordem de matriz 3x3
    print() #Ajuda na formação da matriz pulando de linha
