'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os n primeiros elementos de uma
Sequência de Fibonacci.
ex: 0 > 1 > 1 > 2 > 3 > 5 > 8
'''


num = int(input('Primeiros termos: '))  #Quantidade de termos a mostrar
t1 = 0  #primeiro termo obrigatório
t2 = 1  #Segundo termo obrigatório
cont = 3    #Contador que começa no terceiro termo (os dois primeiros já foram mostrados)
print(f'{t1} > {t2}', end=' > ')    #Os dois primeiros termos
while cont <= num:  #Enquanto o contador não chegar nos termos pedidos, fará a seguinte conta:
    t3 = t1 + t2    #Termo 3 receberá a soma dos últimos dois termos
    t1 = t2         #Termo 1 passa ser o termo 2
    t2 = t3         #Termo 2 passa a ser o termo 3      isso é feito para somar sempres os dois últimos termos, com while fica mais fácil já que ele sempre volta até encontrar o resultado pedido
    print(f'{t3}', end=' > ')   #Mostrando o terceiro termo até o termo pedido
    cont += 1   #Contador recebe mais uma soma
print('fim')
