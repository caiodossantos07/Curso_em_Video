'''
  Crie um código que leia a idade de um atleta e mostre sua categoria de acordo com a seguinte classificação:
- até 9 anos  MIRIM
- até 14 anos INFANTIL
- até 19 anos  JUNIOR
- até 25 anos SENIOR
- acima MASTER
'''
from time import localtime

year = localtime()[0]

birth = int(input('Digite o seu ano de nascimento: '))
age = year - birth
print(f'O atleta tem {age} anos ')

if age <= 9:
    category = 'MIRIM'
    print(f'Classificação {category}')
elif age > 9 and age <= 14:
    category = 'INFANTIL'
    print(f'Classificação {category}')
elif age > 14 and age <= 19:
    category = 'JUNIOR'
    print(f'Classificação {category}')
elif age > 19 and age <= 25:
    category = 'SENIOR'
    print(f'Classificação {category}')
else:
    category = 'MASTER'
    print(f'Classificação {category}')
