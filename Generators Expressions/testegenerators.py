"""
Generator Expressions (ou expressões geradoras) são uma forma de produzir valores sob demanda (preguiçosamente),
um de cada vez, em vez de armazenar todos os valores na memória como uma lista faria.

Elas são parecidas com list comprehensions, mas usam parênteses em vez de colchetes

Você pode obter os valores usando next() ou iterando com for

Uso de memória:
List Comprehension - Armazena todos os itens
Generator Expression - Gera um item por vez (lazy)
"""

minha_lista = [x for x in range(0, 10)]
meu_generator = (x for x in range(0, 10))

print(minha_lista)
print(meu_generator)
# vai printar algo como "<generator object <genexpr> at 0x000001EC73B16D40>"

for numero_que_falta in meu_generator:  # um jeito de usar todos os numeros do generator
    print(numero_que_falta, end=" ")

try:
    next(meu_generator)  # passa para o proximo valor do generator
except StopIteration:
    print("\n\033[31mErro: Não há mais valores no generator\033[m")
# vai dar erro porque já usou todos os valores do generator no loop for acima
