'''
Melhore o DESAFIO 061, perguntando para o usuário
 se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

print('+-=' * 16)
print('GERADOR DE PA')
print('+-=' * 16)
prim = int(input('Inicio: '))
razao = int(input('Razão: '))
termo = prim
cont = 1
total = 0       #Total é = ao total de termos que foi mostrado no programa inteiro.
mais = 10       #Esse 10 é o total de termos iniciais.
while mais != 0:    #Enquanto esse input não for 0, o programa rodará novamente. Se for 0, vai printar o total.
    total = total + mais #total += mais. O total a ser mostrado, vai ser o total que está com 0 + a variável mais que está com 10
    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ? ')) #Esse input será a quantidade de termos a mais a ser mostrados
print(f'Progressão finalizada com {total} termos mostrados.')
