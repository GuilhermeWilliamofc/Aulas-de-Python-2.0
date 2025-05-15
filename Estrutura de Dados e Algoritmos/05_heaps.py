"""
Um heap é uma estrutura de dados baseada em uma árvore binária que satisfaz a propriedade do heap:

Em um min-heap, o menor elemento está no topo (índice 0).

Em um max-heap, o maior elemento está no topo (Python não tem suporte nativo, mas dá pra simular).

Python oferece um min-heap por padrão através do módulo heapq.

Características principais:
Implementado como uma lista.

A cada inserção ou remoção, o heap se reorganiza para manter a ordem correta.

Ideal para filas de prioridade, encontrar o menor elemento rapidamente, etc.
"""

import heapq

dados = [5, 1, 8, 3, 5, 10]
heapq.heapify(dados)
# a função acima transforma a lista em um heap, caso criar uma cópia da lista, será necessário transformar em heap novamente

print(dados)

heapq.heappush(dados, 2)
print(dados)
# para adicionar dados é usado a função heappush

heapq.heappop(dados)
print(dados)
# para remover dados é usado a função heappop (lembra a função pop das listas do python)
# como por padrão o heapq usa um min-heap, o menor valor vai ser removido, e o heap será reorganizado

# caso queira fazer um max-heap usando o heapq tem uma "gambiarra" na qual todos os números da lista são negativos
