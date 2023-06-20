'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.'''

a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))
if a + b > c:
    if a + c > b:
        if b + c > a:
            print('Temos um triângulo')
else:
    print('Não temos um trinângulo')

#Basta fazer a soma entre os dois lados menores.
# Se a soma entre eles for maior que o terceiro lado, então,
# a soma entre qualquer um deles e o terceiro lado (que é o maior) terá o mesmo resultado.
