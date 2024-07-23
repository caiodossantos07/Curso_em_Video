'''
  Crie um código que leia dois lados do trangulo e calcule a hipotenusa através do teorema de pitagoras
  *importação da biblioteca math
'''
'''from math import sqrt as root, pow as pot

co = int(input('Digite o cateto oposto do triângulo: '))
ca = int(input('Digite o cateto oposto do triângulo: '))
hyp = (pot(co, 2)) + pot(ca, 2)
hyp = root(hyp)
print(f'A hipotenusa do triangulo é {hyp}')'''

from math import hypot
co = int(input('Digite o cateto oposto do triângulo: '))
ca = int(input('Digite o cateto oposto do triângulo: '))
hyp = hypot(co, ca)
print(f'A hipotenusa do triangulo é {hyp}')
