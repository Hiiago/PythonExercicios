''' Crie um programa que leia duas notas de um aluno e calcule sua média,
 mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO '''

a = float(input('Nota: '))
b = float(input('Nota: '))

media = (a + b) / 2

if media <= 5:
    print(f'REPROVADO ! Sua média foi de {media:.1f}')
elif media >= 7.0:
    print(f'APROVADO ! Sua média foi de {media:.1f}')
else:
    print(f'RECUPERAÇÃO ! Sua média foi de {media:.1f}')