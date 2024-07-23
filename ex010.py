'''Crie um programa que leia quanto dinheiro a pessoa tem na carteira e converta o valor em dólar'''

saldo = float(input('Qual valor você possui na carteira?: R$ '))
dolar = saldo / 5.44
print(f'Com R${saldo} você consegue comrpar U${dolar:.2f}')
