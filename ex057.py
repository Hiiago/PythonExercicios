'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores:
 'M' ou 'F'. Caso esteja errado, peça a digitação
  novamente até ter um valor correto.
'''


#Ensinado na aula:
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrao com sucesso')



#Forma que fiz:
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = (str(input('Tente novamente: [M/F] '))).upper().strip()[0]

print(f'O sexo informado é {sexo} ')

