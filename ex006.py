#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada(não usar a math)
import math
n = int(input('Digite um número inteiro: ')) 
d = n * 2
t = n * 3
r = n ** (1/2)
print('='*40)
print(f'Número digitado: {n}')
print('='*40)
print(f'Dobro: {d}')
print(f'Triplo: {t}')
print(f'Raiz: {r}')