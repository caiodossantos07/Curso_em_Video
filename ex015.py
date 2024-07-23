'''
  Crie um código que leia a quantidade de Km rodados e de dias usados por um locador de carro. Calcule o valor a pagar
  Considere : R$60 diária R$0,15 por km rodado
'''
day = float(input('Quantos dias de aluguel?: '))
km = float(input('Quantos km rodados?: '))
total = (60 * day) + (0.15 * km)
print('O total a pagar pelo aluguel é de R${}' .format(total))
