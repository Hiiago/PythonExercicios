''' Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.'''

nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
primeiro = nome[0]
ultimo = nome[-1]

print(f'Muito prazer em te conhecer !\n'
      f'{primeiro} é seu primeiro nome\n'
      f'{ultimo} é seu último nome')
