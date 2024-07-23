'''
  Crie um código que some todos impares multiplos de 3 entre 1 e 500
'''
soma, contador = 0, 0
for impar in range(3, 501, 3):
    if impar % 2 == 1:
        print(impar, end=' ')
        soma = soma + impar
        contador = contador + 1
print(f'\nA soma dos {contador} multipos de 3 entre 1 e 500 é {soma}')
