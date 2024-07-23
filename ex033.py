# Crie um código que leia 3 números digitados e mostre o maior e o menor dos números digitados

lista_num = []

for i in range(3):
    num = int(input('Digite um número: '))
    lista_num.append(num)
print(f'O maior número é: {max(lista_num)}')
print(f'O menor número é: {min(lista_num)}')
