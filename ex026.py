'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Frase: ')).upper().strip()
vezes = frase.count('A')
primeira = frase.find('A')
ultima = frase.rfind('A')
print(f'A palavra "A" aparece {vezes} vezes\n'
      f'A 1º posição em que aparece "A" é {primeira+1}\n'
      f'E a última posição é {ultima+1}')
