'''
  Crie um jogo que onde o usuário digita um numero de 0 a 5 e o computador retorna se o foi o número sorteado
'''
from time import sleep
from random import randint
print('-=-' * 20)
print('Vou pensar num número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)

s = randint(0, 5)
n = int(input('Em que número eu pensei? '))
print('PROCESSANO...')
sleep(2)

if n == s:
    print('PARABÊNS! Você conseguiu me vencer!')
else:
    print(f"GANHEI! Eu pensei no número {s} e não no {n}")
