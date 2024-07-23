#Crie um conversor de metros para as demais escalas de medida

m = float(input('Digite uma medida em metros: '))
mm = m * 1000
cm = m * 100
dc = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('='* 40)
print(f'Medida digitada de {m:}m corresponde a:')
print(f'='* 40)
print(f'{mm:.0f}mm')
print(f'{cm:.0f}cm')
print(f'{dc:.0f}dc')
print(f'{m:}m')
print(f'{dam:}dam')
print(f'{hm:}hm')
print(f'{km:}km')
