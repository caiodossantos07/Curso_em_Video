# Crie um código que leia o salário de um funcionário, se esse salário for superio a R$1250 aplique um aumento de 10%
# Se  o salário for inferio a R$1250 aplique um aumento de 15%

sal = float(input('Digite o salário do funcionário: R$'))

if sal < 1250:
    sal = sal * 1.15
    print(f'O funcionário passará a ganhar R${sal:.2f}')
else:
    sal = sal * 1.1
    print(f'O funcionário passará a ganhar R${sal:.2f}')
