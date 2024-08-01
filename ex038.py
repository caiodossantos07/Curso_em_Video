'''
  Crie um código que leia dois números inteiros e diga se:
  - O primeiro valor é maior
  - O segundo valor é maior
  - Os dois são iguais
'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O primeiro número é maior')
elif n1 < n2:
    print(f'O segundo número é maior')
else:
    print(f'Os dois números são iguais')
