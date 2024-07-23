# Crie um código que  pergunte a distância de uma viagem em km e calcule o preço da pasagem, cobrando
# R$0,50 por km para viagens até 200km e R$0,45 para viagens acima de 200km

distancia = int(input('Digite a distância percorrida em km: '))
if distancia <= 200:
    preco = distancia * .50
else:
    preco = distancia * .45
print(f'O preço da passagem é R${preco:.2f}')
