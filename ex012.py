'''Crie um programa que leia o valor de um produto e aplique o desconto de 5%'''

price = float(input("Digite o valor do produto: R$"))
p_discount = price * 0.95

print(
    f'O produto que custava R${price:.2f}, com desconto de 5% vai custar R${p_discount:.2f}')
