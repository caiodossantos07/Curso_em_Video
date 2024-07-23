'''
  Crie um código que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
'''
numbers = input('Digite um número de 0 a 9999: ')
num_list = [0, 0, 0, 0]
# Inverte a ordem da string
invert_nums = numbers[::-1]
c = 3
for invert_num in invert_nums:
    num_list[c] = int(invert_num)
    c -= 1
print(f'Milhar: {num_list[0]}')
print(f'Centena: {num_list[1]}')
print(f'Dezena: {num_list[2]}')
print(f'Unidade: {num_list[3]}')
