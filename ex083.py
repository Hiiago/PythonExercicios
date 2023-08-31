'''
 Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

#Minha fórmula:

palavra = list(str(input('Digite a expressão: ')))

if palavra.count('(') - palavra.count(')') == 0:
    print('Expressão correta.')
else:
    print('Expressão incorreta. ')

#Fórmula do professor:
expr = str(input('Digite sua expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão correta.')
else:
    print('Expressão incorreta.')


