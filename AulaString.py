'''
  Manipulando Texto
'''
frase = 'Curso em Video Python'
frase2 = '   Aprenda Python  '
'''1
print(frase[9:13])
# >>> 'Vide'
#Vai do index 9 até o 12
'''
'''2
print(frase[9:21])
# >>> Video Python
#Vai do index 9 até o 20
'''
'''3
print(frase[9:21:2])
# >>> VdoPto
#Vai do Index 9 até o 20 pulando 1
'''
'''4
print(frase[:5])
# >>> Curso
#Vai do index 0 até o 4
'''
'''5
print(frase[9::3])
# >>> VePh
#Vai do index 9 até o final pulando 2
'''
'''6
print(len(frase))
# >>> 21
#Printa o tamanho do frase
'''

'''7
print(frase.count('o'))
# >>> 3
#Retorna quantas vezes aparece a letra 'o' na frase
'''
'''8
print(frase.count('o', 0, 13))
# Retorna quantas vezes aparece a letra 'o' o index 0 ao 12
'''
'''9
print(frase.find('deo'))
# >>> 11
# Indica que o trecho 'deo' inicia na posição 11
'''
'''10
print(frase.find('Android'))
# >>> -1
# Indica que o trecho 'Android' não existe na frase
'''

'''11
print('Curso' in frase)
# >>> True
# Indica que o trecho 'Curso' existe na frase
'''
'''12
print(frase.replace('Python', 'Android'))
print(frase)
# >>> Curso em Video Android
# >>> Curso em Video Python
# Retorna a substituição do trecho 'Python' por 'Android', porém não altera na variável
'''
'''13
print(frase.upper())
# >>> CURSO EM VIDEO PYTHON
# Retorna todos caracteres da frase em maiuscolo, não altera na variável
'''
'''14
print(frase.lower())
# >>> curso em video python
# Retorna todos caracteres da frase em minúsculo, não altera na variável
'''
'''15
print(frase.capitalize())
# >>> Curso em video python
# Retorna o primeiro caracter da frase em maiúscula os demais em minúsculo
'''
'''16
print(frase.title())
# >>> Curso Em Video Python
# Retorna o primeiro caracter da cada palavra em maiúscula os demais em minúsculo
'''
'''17
print(frase2)
print(frase2.strip())
# >>>    Aprenda Python
# >>>Aprenda Python
# Remove os espaços antes e depois da frase
'''
'''18
frase2.rstrip())
# Remove os espaços a direita
frase2.lstrip())
# Remove os espaços a esquerda
'''
'''19
teste = frase.split()
print(teste)
print(type(teste))
# >>> ['Curso', 'em', 'Video', 'Python']
# >>> <class 'list' >
# O split divide a frase pelos espaços e criando uma lista se armazenado em uma variável
'''
'''20
teste = ['Curso', 'em', 'Video', 'Python']
print('-'.join(teste))
print(' '.join(teste))
# >>> Curso-em-Video-Python
# >>> Curso em Video Python
# O join une uma lista podendo ser adicionado '-' espaço em branco ou qualquer outro caracter
'''
