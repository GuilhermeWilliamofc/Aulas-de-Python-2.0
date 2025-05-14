# Criando uma pilha
"""Uma stack (pilha) é uma estrutura de dados do tipo LIFO – Last In, First Out, ou seja,
o último elemento que entra é o primeiro a sair. Pense em uma pilha de pratos: você coloca um prato por cima e retira também por cima.

Tem duas operações principais:

push(item): adiciona um item ao topo da pilha. no caso desse script eu chamei de adicionar()

pop(): remove o item do topo da pilha. no caso desse script eu chamei de remover()
"""


class Pilha:
    def __init__(self):
        self.itens = []

    def adicionar(self, valor):
        self.itens.append(valor)

    def tamanho(self) -> int:
        return len(self.itens)

    def remover(self):
        if self.tamanho != 0:
            return self.itens.pop()

    def printar(self):
        print(self.itens)


minha_pilha = Pilha()
minha_pilha.adicionar("item 1")
minha_pilha.adicionar("item 2")
minha_pilha.adicionar("item 3")
minha_pilha.adicionar("item 4")
minha_pilha.printar()

minha_pilha.remover()
minha_pilha.remover()
minha_pilha.printar()
