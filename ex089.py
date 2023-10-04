'''
Crie um programa que leia nome e duas notas de vários alunos
 e guarde tudo em uma lista composta. No final, mostre um boletim
  contendo a média de cada um e permita que o usuário possa mostrar
   as notas de cada aluno individualmente.
'''

ficha = []
while True:
    nome = str((input('Nome: ')))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2   #Calculo da media
    ficha.append([nome, [n1, n2], media]) #Adicionando os dados a lista ficha sendo eles [0, 1, 2]
    resp = str(input('Continuar ? [S/N] '))
    if resp in 'Nn': #se a resposta for N ou n:
        break   # Pare o programa
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}') #Nº nome e nota que será mostrado
print('-'*26)
for i, a in enumerate(ficha): #Para cada indice de aluno na numeração de ficha
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') #Mostrando os dados de numeração, nome e notas
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno ? [999 interrompe]: ')) #variavel que pergunta o numero dos alunos que quer ver as notas
    if opc == 999:  #se for 999 programa será parado
        break
    if opc <= len(ficha) - 1: #Se for numero que tem na lista:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}') #Será mostrado o nome do aluno e as notas
print('<<<<VOLTE SEMPRE!>>>>')
