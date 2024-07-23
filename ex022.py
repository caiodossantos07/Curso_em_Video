'''
  Crie um código que solicite um nome ao usuário e apresente os seguintes retornos:
  1. Nome todo em maiússculo
  2. Nome todo em minuscula
  3. Total de letras do nome
  4. Primeiro nome e quantidade de letras
'''
name = input('Digite um nome: ').strip()
print(f'=' * 40)
print('Analisando seu nome...')
print(f'=' * 40)
print(f'Seu nome maiúsculo é: {name.upper()}!')
print(f'Seu nome minúsculo é: {name.lower()}!')
# print(f'Seu nome tem ao todo: {len(name.replace(" ", ""))} letras!')
print(f'Seu nome tem ao todo: {len(name) - name.count(" ")} letras!')
print(
    f'Seu primeiro nome é {name.split()[0]} e ele tem {len(name.split()[0])} letras!')
print(
    f'Seu último nome é {name.split()[-1]} e tem {len(name.split()[-1])} letras!')
