'''
  Crie um código que leia um ano de nascimento e retorne:
  - Quantos anos a pessoa tem
  - Quando foi ou será o alistamento
  - Ano de alistamento
'''
from time import localtime

birth = int(input('Digite o ano de nascimento: '))

year = localtime()[0]
age = year - birth
age_alist = birth + 18

print(f'Quem nasceu em {birth} tem {age} anos em {year}  ')

# pass
if age > 18:
    print(f'Você deveria ter se alistado há {year - age_alist}')
    print(f'Seu alistamento foi em {age_alist}')
# future
elif age < 18:
    print(f'Faltam {age_alist - year} anos para seu alistamento')
    print(f'Seu alistamento será em {age_alist}')
else:
    print(f'Você deve se alistar imediatamente')
