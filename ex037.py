# Crie um códigoque leia um número inteiro digitado pelo usuário e faça a conversão para:
# 1 - para binário
# 2 - para octal
# 3 - para hexadecimal

# Função de conversão para  binário
def tobinary(x):
    if x == 0:
        print(f'{x} convertido para binário é: 0')
        return

    bits = []
    while x > 0:
        bits.append(str(x % 2))  # Adiciona ao final da lista
        x = x // 2
    bits.reverse()  # Reverte a lista para a ordem correta
    binary_string = ''.join(bits)
    print(f'{num} convertido para binário é: {binary_string}')
# Fim da função binário

# Função de conversão para  octal


def tooctal(x):
    if x < 8:  # Trata o caso de entradas menores que 8
        octal_string = str(x)
    else:
        octal = []
        while x > 0:
            octal.append(str(x % 8))  # Adiciona a lista e converte para string
            x = x // 8
        octal.reverse()  # Reverte a lista para a ordem correta
        octal_string = ''.join(octal)

    print(f'{num} convertido para octal é: {octal_string}')
# Fim da função octal

# Função de conversão para hexadecimal


def tohexa(x):
    if x == 0:
        # Se o número for 0, imprime diretamente e retorna
        print(f'{num} convertido para hexadecimal é: {x}')
    else:
        hexa = []  # Lista para armazenar os dígitos hexadecimais
        # Dicionário para mapeamento dos dígitos hexadecimais
        hexa_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

        # Loop para calcular os dígitos hexadecimais
        while x > 0:
            remainder = x % 16  # Calcula o resto da divisão por 16
            if remainder in hexa_dict:
                # Se o resto está no dicionário, usa o valor mapeado
                hexa.append(hexa_dict[remainder])
            else:
                # Caso contrário, adiciona o resto convertido em string
                hexa.append(str(remainder))

            x = x // 16  # Atualiza o valor de x para a próxima iteração

        hexa.reverse()  # Reverte a lista para a ordem correta
        # Junta os elementos da lista em uma string
        hexa_string = ''.join(hexa)
        # Imprime o resultado
        print(f'{num} convertido para hexadecimal é: {hexa_string}')


num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão')
print('[1] - para binário \n[2] - para octal \n[3] - para hexadecimal')
option = input('Opção: ')

if option == '1':
    tobinary(num)
elif option == '2':
    tooctal(num)
elif option == '3':
    tohexa(num)
else:
    print('"[Erro] Opção inválida!"')
