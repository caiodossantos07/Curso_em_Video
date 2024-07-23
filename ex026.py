'''
  Crie um código que leia uma frase e mostre:
  *Quantas vezes foi digitado a letra "A";
  *Em que posição ela aparece pela primeira vez;
  *Em que posição ela aparece pela última vez.
'''

phrase = str(input('Digite uma frase: ').lower().capitalize())
print(f'Frase digitada:\n{phrase}')
print(f'A letra "A/a" foi digitada {phrase.count("a")} vezes')
print(
    f'A letra "A/a" aparece pela primeria vez na posição: {phrase.find("a") + 1}')
print(
    f'A letra "A/a" aparece pela última vez na posição: {phrase.rfind("a") + 1}')

'''
phrase = str(input('Digite uma frase: ').lower().capitalize())
a_times = phrase.count('a')
a_first = (phrase.find('a') + 1)
a_last = (phrase.rfind('a') + 1)
print(f'Frase digitada:\n{phrase}')
print(f'A letra "A/a" foi digitada {a_times} vezes')
print(f'A letra "A/a" aparece pela primeria vez na posição: {a_first}')
print(f'A letra "A/a" aparece pela última vez na posição: {a_last}')
'''
