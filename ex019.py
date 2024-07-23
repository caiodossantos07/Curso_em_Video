
# Crie um código que leia 4 nomes e sorteie um entre os 4

# Meu código
import random

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
s = random.randint(0, len(lista)-1)
print(f'O nome sorteado foi "{lista[s]}"')

"""
#**Código do guanabara
import random
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
s = random.choice(lista)
print(f'O nome sorteado foi "{s}"')
"""
