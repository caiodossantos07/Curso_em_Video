'''
  Crie um código que leia um nome completo e apresente o primeiro e o último nome
'''

name = input('Digite um nome completo: ')
list_name = name.split()
print(f'O primeiro nome é: {list_name[0]}')
print(f'O último nome é: {list_name[-1]}')
