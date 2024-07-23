'''
  Crie um código que leia 4 nomes e mostre eles em ordem sorteada
'''
from random import shuffle

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')

lista = [n1, n2, n3, n4]
shuffle(lista)
# print('A ordem é:', lista[0], lista[1], lista[2], lista[3],)
print(f'=' * 20)
print('Ordem sorteada: ')
print(f'=' * 20)
print(f'\n1º) {lista[0]} \n2º) {lista[1]} \n3º) {lista[2]} \n4º) {lista[3]}')
