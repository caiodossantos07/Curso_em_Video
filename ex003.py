'''
n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')
soma = n1 + n2
print(f'A soma dos números é {soma}')
O erro no código ocorre pq o input é armazenado na váriavél como string. Para corrigir é necessário fazer a converção(casting) para int ou float conforme exemplo abaixo 
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2
print(f'A soma entre {n1} e {n2} é {soma}')