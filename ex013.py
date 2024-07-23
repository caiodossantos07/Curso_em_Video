''' 
  Crie um código que leia um salário e o aumente em 15%
'''

sal = float(input('Digite o valor do salário: R$'))
n_sal = sal * 1.15
print(
    f'O funcionário que ganhava R${sal: .2f}, com aumento de 15% passa a ganhar R${n_sal: .2f}')
