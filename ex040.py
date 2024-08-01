'''
  Crie um código que leia duas notas tiradas por um aluno calcule a média e diga que:
  - Aprovado se média maior ou igual a 7;
  - reprovado se média menor que 5; 
  - De recuperação se média entre 7 e 5.
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
average = (n1 + n2) / 2

print(f'Tirando {n1} e {n2}, a média é {average}')
if average >= 7:
    print('O aluno está APROVADO.')
elif average < 5:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está em RECUPERAÇÃO.')
