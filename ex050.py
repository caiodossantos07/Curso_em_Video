'''
  Crie um código que leia 6 números inteiros e some apenas os pares
'''
soma = 0
for n in range(1, 7):
    pares = int(input('Digite um número inteiro: '))
    if pares % 2 == 0:
        soma += pares
print(f'A soma dos pares digitados é {soma}')
