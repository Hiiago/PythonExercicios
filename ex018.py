'''leia um ângulo na tela e o valor do:
seno, cosseno e tangente desse ângulo'''


from math import sin, cos, tan, radians
angulo = float(input('digite um angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {(seno):.2f}\n'
      f'O ângulo de {angulo} tem o COSSENO de {(cosseno):.2f}\n'
      f'O ângulo de {angulo} tem a TANGENTE de {(tangente):.2f}')
