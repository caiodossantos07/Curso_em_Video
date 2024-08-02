'''
  Crie uma calculadora e IMC considerando:
  - abaixo de 18.5: Abaixo do peso
  - Entre 18.5 e 25: Peso ideal
  - 25 até 30: Sobrepeso
  - 30 até 40: Obesidade
  - Acima de 40: Obesidade mórbida
'''

weight = float(input('Digite seu peso: '))
height = float(input('Digite sua altura: '))

imc = weight / (height ** 2)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print(f'Você está abaixo do peso ideal')
elif imc >= 18.5 and imc < 25:
    print(f'Você está no peso ideal')
elif imc >= 25 and imc < 30:
    print(f'Você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print(f'Você está com obesidade')
else:
    print(f'Você está com obesidade mórbida')
