'''
  Crie um programa que leia um numero real e retorne apenas sua parte inteira
  //***importação de biblioteca e ou função especifica e atribuição de nome para função 
'''
from math import trunc as inteiro
real = float(input('Digite um numero real: '))
i = inteiro(real)
print(f'O valor digitado foi {real} e sua parte inteira é {i}')
