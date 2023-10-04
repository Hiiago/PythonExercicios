'''
Faça um programa que leia nome e peso de várias pessoas,
 guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

temp = []   #Lista temporária que vai guardar os dados antes de ir pra principal
princ = []  #lista principal
mai = men = 0   #Maior e menor começando com 0

while True: #Enquanto verdadeiro
    temp.append(str(input('Nome: ')))   #nome:
    temp.append(float(input('Peso: '))) #peso:

    if len(princ) == 0: #Se nao cadastrei ninguem ainda (nao tenho ninguem na lista)
        mai = men = temp[1] #O maior e menor serão o mesmo que o peso (temp[1])
    else:   #Se nao for o primeiro
        if temp[1] > mai:   #Se o temp[1] (peso) for maior que o maior peso:
            mai = temp[1]   #O maior peso passa a ser o temp[1] (peso que está sendo maior).
        if temp[1] < men:   #Se o temp[1] (peso) for menor que o menor peso:
            men = temp[1]   #O menor peso passa a ser o temp[1] (peso que está sendo menor).

    princ.append(temp[:])  #Copiando os dados temporario para o principal
    temp.clear()    #Deletando a lista temporaria para mostrar a lista principal sem ser mostrados juntos

    resp = str(input('Continuar ? [S/N] ')) #Continuar ?
    if resp in 'Nn':    #Se a resposta for N ou n:
        break           #O programa é parado

print('==' * 30)    #Pulando linha
print(f'Ao todo você cadastrou {len(princ)} pessoas.')  #Quantas pessoas foram cadastradas. O len funciona como um contador
print(f'O maior peso foi de {mai}kg. Peso de ', end='') #Mostrando maior peso e puxando o resultado do print de for com end=''
for p in princ: #Para cada pessoa no principal (vai varrer o principal que tem lista dentro de lista e pegar cada uma das listas jogando em ''p'')
    if p[1] == mai: #Se p[1] (peso) for igual ao maior peso:
        print(f'[{p[0]}] ', end='') #Vai mostrar a pessoa com maior peso
print() #print para pular para a linha de baixo
print(f'O menor peso foi de {men}kg. Peso de ', end='') #Mostrando menor peso e puxando o resultado do print de for com end=''
for p in princ: #Para cada pessoa no principal (vai varrer o principal que tem lista dentro de lista e pegar cada uma das listas jogando em ''p'')
    if p[1] == men: #Se p[1] (peso) for igual ao menor peso:
        print(f'[{p[0]}] ', end='') #Vai mostrar a pessoa com menor peso
