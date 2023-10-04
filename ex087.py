'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  #Lista com 3 listas dentro com 3 valores em cada lista (para nao usar append) para depois substituir os 0 por valores
spar = mai = scol = 0   #Soma par; maior; soma coluna = 0

#For de alimentação. o que vou colocar os valores dentro da matriz
for l in range(0, 3):   #laço de linhas
    for c in range(0, 3):   #Laço de colunas
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) #esses valores vão para cada linha e coluna indicadas

print('=='*25)  #dividindo linha

#For para mostrar a estrutura na tela
for l in range(0, 3): #Laço de linhas
    for c in range(0, 3): #laço de colunas
        print(f'[{matriz[l][c]:^5}] ', end='')  #Mostrando os valores em ordem de matriz 3x3
        if matriz[l][c] % 2 == 0:   #Verificando os números pares
            spar += matriz[l][c]    #Somando os números pares
    print() #Ajuda na formação da matriz pulando de linha
print('=='*25)
print(f'A soma dos valores pares é {spar}') #Mostrando na tela a soma dos números pares
for l in range(0, 3):   #for de linhas
    scol += matriz[l][2]  #Somando os valores da terceira coluna
print(f'A soma dos valores da terceira coluna é {scol}') #E mostrando esse valor
for c in range(0, 3):   #for de colunas
    if c == 0:  #Se a coluna for igual 0
        mai = matriz[1][c]  #então a linha 2 recebe 0
    elif matriz[1][c] > mai:    #se a linha 2 for maior que maior:
        mai = matriz[1][c]  #linha 2 recebe o maior valor
print(f'O maior valor da segunda linha é {mai}')
