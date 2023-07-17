'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

#Feito no vídeo:
print('=' * 30)
print(f'         BANCO CEV')
print('=' * 30)
valor = int(input('Qual valor deseja sacar? R$'))
total = valor     #Montante
cedula = 50       #Desse montante vou tirar 50 reais quantas vezes forem necessárias
totcedu = 0       #Total de cédulas que o caixa tem que dar
while True:       #Esse lopp vai ser quebrado quando acabar o valor
      if total >= cedula:
            total -= cedula
            totcedu += 1       #Cada vez que der para tirar 50 do total, adiciona o + 1 ao total de cedula
      else:                    #Se não:
            if totcedu > 0:
                  print(f'Total de {totcedu} cédulas de R${cedula}.')
            if cedula == 50:        #Se a cedula atual = 50:
                  cedula = 20       #A proxima cedula = 20
            elif cedula == 20:      # e assim por diante
                  cedula = 10
            elif cedula == 10:
                  cedula = 1
            totcedu = 0
            if total == 0:          #Se o total = 0: pare o programa
                  break
print('='*30)
print('Volte sempre ao BANCO CEV!')
#O programa vai pegar o montande do dinheiro que é o total e vai tirando R$50 até não dar mais
# Depois vai tirando notas de 20 até não dar mais e assim por diante


#Como eu fiz:
print('='*41)
print('             Caixa Python\n'
      'Notas disponíveis: R$50, R$20, R$10 e R$1')
print('='*41)
valor = int(input('Qual valor será sacado ? R$'))
n50 = n20 = n10 = n1 = 0
while True:
      if valor / 50:
            n50 = valor // 50
            print(f'Total de {n50} cédulas de R$50.')
      if valor / 20:
            n20 = (valor - (n50*50)) // 20
            print(f'Total de {n20} cédulas de 20.')
      if valor / 10:
            n10 = (valor - (n50*50) - (n20*20)) // 10
            print(f'Total de {n10} cédulas de R$10.')
      if valor / 1:
            n1 = (valor - (n50*50) - (n20*20) - (n10*10)) // 1
            print(f'Total de {n1} cédulas de R$1.')
            break
print('='*41)

#Resolução:  cada valor está sendo calculado subtraindo a divisão do valor anterior
#Se o valor for divisivel por 50: a variável n50 recebe o valor dividido por 50, que é uma cédula disponível
#Se for por 20: n20 recebe o valor dividido anterior e subtrai pelo valor e dividindo por 20
#Sempre que tiver mais valores, a lógica continua adicionando os valores anteriores e dividindo pela próxima cédula.