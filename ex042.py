# Crie um código que leia o comprimento de 3 retas e diga se é possivel formar um triângulo e o tipo de triangulo
print('-=-' * 15)
print('Analisador de triângulo')
print('-=-' * 15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        form = 'EQUILÁTERO'
    elif r1 != r2 != r3 != r1:  # PODE SER REMOVIDO O AND E FEITO DESSA MANEIRA
        form = 'ESCALENO'
    else:
        form = 'ISÓCELES'
    print(f'Os segmentos acima PODEM formar um triângulo {form}')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
