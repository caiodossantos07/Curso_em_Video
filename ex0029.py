'''
  Crie um código que leia a velocidade de um carro e se ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
'''

speed = float(input('Digite a velociadade do carro: '))
if speed > 80:
    penalty = (speed - 80) * 7
    print('MULTADO! Você excedeu o limite de velocidade permitdo que é de 80km/h')
    print(f'Você deve pagar uma multa de R${penalty}')
print('Tenha um bom dia! Dirija com segurança!')
