'''
  Crie um código que faça uma contagem regressiva de 10 a 0
'''
from time import sleep
for num in range(10, -1, -1):
    print(num)
    sleep(1)
print('Bum! Bum! Bum!')
