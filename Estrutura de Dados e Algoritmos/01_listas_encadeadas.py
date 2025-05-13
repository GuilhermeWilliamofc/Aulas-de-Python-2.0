# Nós (vulgo Node)
# 1. Valor - pode ser strings, inteiros, objetos...
# 2. O próximo nó

# esse script é um teste simples de lista encadeada


class ListaEncadeadaNó:
    def __init__(self, valor, proximo_nó=None) -> None:
        self.valor = valor
        self.proximo_nó = proximo_nó


nó_1 = ListaEncadeadaNó(3)
nó_2 = ListaEncadeadaNó(7)
nó_3 = ListaEncadeadaNó(10)
nó_4 = ListaEncadeadaNó(77)

nó_1.proximo_nó = nó_2
nó_2.proximo_nó = nó_3
nó_3.proximo_nó = nó_4

nó_atual = nó_1

while True:
    print(nó_atual.valor, "->", end=" ")
    if nó_atual.proximo_nó is None:
        print("None")
        break
    nó_atual = nó_atual.proximo_nó
