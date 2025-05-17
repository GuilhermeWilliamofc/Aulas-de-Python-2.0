"""
List Comprehension é uma forma concisa e elegante de criar listas a partir de outras sequências (como listas, tuplas, ranges, etc.) usando uma sintaxe compacta.
"""

lista_precos = [300, 1500, 576, 2100, 200]

# sem list comprehension

# caso 1
nova_lista_precos = []
for preco in lista_precos:
    nova_lista_precos.append(preco * 2)
print(nova_lista_precos)

# caso 2
imposto = []
for preco in lista_precos:
    if preco > 1000:
        imposto.append(preco * 0.5)
print(imposto)

# com list comprehension

# caso 1
nova_lista_precos2 = [preco * 2 for preco in lista_precos]
print(nova_lista_precos2)

# caso 2
imposto2 = [preco * 0.5 for preco in lista_precos if preco > 1000]
print(imposto2)
