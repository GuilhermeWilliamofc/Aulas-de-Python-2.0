lista_produtos = ['iphone', 'ipad', 'airpod', 'macbook']
tupla_produtos = ('iphone', 'ipad', 'airpod', 'macbook')
conjunto_produtos = {'iphone', 'ipad', 'airpod', 'macbook'}

# pegar valores
print(f'o primeiro valor da lista é {lista_produtos[0]}')
print(f'o primeiro valor da tupla é {tupla_produtos[0]}')
print(f'o primeiro valor do set é {list(conjunto_produtos)[0]}') # não tem como "printar" um valor especifico num set/conjunto, só se transformar em uma lista/tupla

# adicionar valores
lista_produtos.append('apple watch') 
# não tem como adicionar valores numa tupla pois ela é imutável
conjunto_produtos.add('apple watch')

print()
print(f'com o novo valor a lista agora é "{lista_produtos}"')
print(f'com o novo valor a tupla agora é "{tupla_produtos}"')
print(f'com o novo valor o set agora é "{conjunto_produtos}"') # os sets/conjuntos embaralham a ordem pré estabelecida

# valores repetidos
lista_produtos = ['iphone', 'ipad', 'airpod', 'macbook', 'macbook']
tupla_produtos = ('iphone', 'ipad', 'airpod', 'macbook', 'macbook')
conjunto_produtos = {'iphone', 'ipad', 'airpod', 'macbook', 'macbook'}

print()
print(f'com valores repetidos a lista agora é "{lista_produtos}"')
print(f'com valores repetidos a tupla agora é "{tupla_produtos}"')
print(f'com valores repetidos o set agora é "{conjunto_produtos}"') # os sets/conjuntos remove valores repetidos

lista_produtos = list(set(lista_produtos)) # um dos usos dos sets/conjuntos, remover valores repetidos de listas
print()
print(f'com valores repetidos a lista agora é "{lista_produtos}"')
