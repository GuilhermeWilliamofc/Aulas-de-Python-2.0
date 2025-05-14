# Criando uma fila
"""
Em Python, uma fila (queue) é uma estrutura de dados do tipo FIFO – First In, First Out, ou seja,
o primeiro item que entra é o primeiro a sair, como uma fila de pessoas no banco.

Tem duas operações principais:

enqueue (enfileirar): adiciona um item no final da fila. no caso desse script eu chamei de adicionar_na_fila()

dequeue (desenfileirar): remove o item do início da fila. no caso desse script eu chamei de remover_da_fila()
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


class Fila:
    def __init__(self):
        self.entrada_de_dados = Pilha()
        self.saida_de_dados = Pilha()

    def tamanho(self):
        return self.entrada_de_dados.tamanho() + self.saida_de_dados.tamanho()

    def adicionar_na_fila(self, item):
        self.entrada_de_dados.adicionar(item)

    def remover_da_fila(self):
        if not self.saida_de_dados.itens:  # se a pilha não está vazia
            while self.entrada_de_dados.itens:
                self.saida_de_dados.adicionar(
                    self.entrada_de_dados.remover()
                )  # o item removido da pilha entrada de dados é adicionado na pilha saida de dados, ficando em formato de fila
                # os primeiros itens ficam no final da lista e os últimos no começo
                # ex: uma lista [1,2,3] entra nesse metodo e volta como [3,2]
        return self.saida_de_dados.remover()

    def printar_fila(self):
        if len(self.entrada_de_dados.itens) != 0:
            print(
                self.entrada_de_dados.itens[::-1]
            )  # printa a lista invertida, se bem que acho q seria mais fácil usar isso para o remover_da_fila...
        else:
            self.saida_de_dados.printar()


minha_fila = Fila()
clientes = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4", "Cliente 5"]

for cliente in clientes:
    # fiz esse for para não precisar escrever uma linha para cada cliente novo
    minha_fila.adicionar_na_fila(cliente)

minha_fila.printar_fila()

minha_fila.remover_da_fila()
minha_fila.printar_fila()

minha_fila.remover_da_fila()
minha_fila.printar_fila()
