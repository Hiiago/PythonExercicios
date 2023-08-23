'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

tupla = ('mouse', 'teclado', 'monitor', 'headset',
         'cooler', 'processador', 'placa de video',
         'fans rgb', 'memoria ram', 'ssd', 'nvme', 'placa mae') #Tupla em que trabalharemos as palavras


for i in tupla: #Para cada indice (palavra) em tupla:
    print(f'\nNa palavra {i.upper()} temos: ', end='') #Mostre cada palavra dentro da tupla
    for letra in i: #Para cada letra em indice(palavra):
        if letra.lower() in 'aeiou': #Se a letra de cada indice tiver 'a e i o u':
            print(letra.upper(), end=' ')   #Mostre somente essas letras.

'''
primeiro for analisa cada elemento da tupla
segundo for pega cada letra na tupla e ve se tem as vogais e mostra 
'''
