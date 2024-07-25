# Crie um código para aprovar empréstimos para compra de uma casa.
# Solicite o valor da casas, saláriodo comprador e em quantos anos ele irá pagar.
# A prestação mensal não pode exceder 30% do salário senão o empréstimo será negado.

house_price = float(input('Digite o valor da casa: R$'))
salary = float(input('Digite o salário: R$'))
time = (12 * int(input('Digite em quantos anos irá pagar: ')))
installment = house_price / time
if installment <= (salary * 0.3):
    result = 'APROVADO'
else:
    result = 'REPROVADO'
print('-=' * 20)
print(f'{"EMPRÉSTIMO":>20} {result:<20}')
print('-=' * 20)
