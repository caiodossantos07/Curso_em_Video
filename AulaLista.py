
# Criação de uma lista
lista = [1, 2, 3]
'''
# Adicionando elementos
lista.append(4)
print("Após append:", lista)  # Saída: [1, 2, 3, 4]

lista.insert(1, 'a')
print("Após insert:", lista)  # Saída: [1, 'a', 2, 3, 4]

lista.extend([5, 6])
print("Após extend:", lista)  # Saída: [1, 'a', 2, 3, 4, 5, 6]

# Removendo elementos
lista.remove('a')
print("Após remove:", lista)  # Saída: [1, 2, 3, 4, 5, 6]

item = lista.pop()
print("Após pop:", lista)  # Saída: [1, 2, 3, 4, 5]
print("Item removido:", item)  # Saída: 6

item = lista.pop(1)
print("Após pop(1):", lista)  # Saída: [1, 3, 4, 5]
print("Item removido:", item)  # Saída: 2

# Outros métodos
index = lista.index(3)
print("Index de 3:", index)  # Saída: 1

count = lista.count(4)
print("Count de 4:", count)  # Saída: 1

lista.sort()
print("Após sort:", lista)  # Saída: [1, 3, 4, 5]

lista.reverse()
print("Após reverse:", lista)  # Saída: [5, 4, 3, 1]

copia = lista.copy()
print("Cópia da lista:", copia)  # Saída: [5, 4, 3, 1]

lista.clear()
print("Após clear:", lista)  # Saída: []
'''
