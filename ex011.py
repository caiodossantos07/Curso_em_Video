'''Crie um programa que leia as dimensoes de uma parede em metros e calcule sua área e a quantidade de tinta necessária 
para pinta-la, considere que cada litro pinta 2m²'''

alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = alt * larg
litros = area / 2
print(f'Sua parede tem as dimensões de  {alt}x{larg} e uma área de {area}m²')
print(f'Serão necessários {litros:.2f}l de tinta para pinta-la')
