'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = str(input('Nome: ')).strip()
print(nome.upper())
print(nome.lower())
letras = len(nome) - nome.count(' ')
nome1 = nome.split()
print(f'{nome} ao todo tem {letras} letras\n'
      f'{nome1[0]} tem {len(nome1[0])} letras')
