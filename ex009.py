#Crie um algoritmo que imprima a tabuada de um número digitado pelo usuário:

n = int(input('Digite um numéro inteiro:'))

print(f'='* 40)
print(f'Tabuada do {n}')
print(f'='* 40)
def tabuada (n):
  for i in range(1,11):
    result = n * i
    print(f'{n} x {i} = {result}')

tabuada(n)