"""
4. Na fila circular ligada, identifique para onde aponta fim.proximo apos inserir A, B e C.
Depois de retirar A, qual no passa a ser o primeiro? Explique tambem o caso de retirar o unico no.
"""

class No:
    def __init__(self, valor, proximo = None):
        self.valor = valor
        self.proximo = proximo

class Fila_Circular_Ligada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    def estaVazia(self):
        return self.quantidade == 0

    def obterQuantidade(self):
        return self.quantidade

    def inserir(self, valor):
        novo = No(valor)

        # se estiver vazia: o unico no aponta para ele mesmo
        if self.estaVazia():
            self.inicio = novo
            self.fim = novo
            self.fim.proximo = self.inicio
        # se estiver com pelo menos 1 elemento
        elif self.fim is not None and self.inicio is not None:
            self.fim.proximo = novo
            self.fim = novo
            self.fim.proximo = self.inicio  # o novo ultimo fecha o circulo

        self.quantidade += 1

    def remover(self):
        if self.estaVazia() or self.inicio is None or self.fim is None:
            return

        removido = self.inicio

        # Se existir apenas um elemento: a fila volta a ficar vazia
        if self.quantidade == 1:
            self.inicio = None
            self.fim = None
        # Senao: o segundo vira o primeiro e o fim passa a apontar para ele
        else:
            self.inicio = removido.proximo
            self.fim.proximo = self.inicio

        # solta o no removido para nao ficar apontando para a fila
        removido.proximo = None

        self.quantidade -= 1
        return removido.valor

    def imprimir(self):
        if self.estaVazia():
            print("Fila Vazia")
            return

        atual = self.inicio

        for i in range(self.quantidade):
            if atual is None:
                return

            print(atual.valor, end=" ")
            atual = atual.proximo

        print()

    def mostrarPonteiros(self):
        if self.estaVazia() or self.inicio is None or self.fim is None or self.fim.proximo is None:
            print("inicio = None | fim = None")
            return

        print(f"inicio = {self.inicio.valor} | fim = {self.fim.valor} | fim.proximo = {self.fim.proximo.valor}")


if __name__ == "__main__":
    fila = Fila_Circular_Ligada()
    fila.inserir("A")
    fila.inserir("B")
    fila.inserir("C")

    print("Depois de inserir A, B e C:")
    fila.imprimir()
    fila.mostrarPonteiros()  # fim.proximo aponta para A (o inicio)

    print("\nRemovendo A:")
    fila.remover()
    fila.imprimir()
    fila.mostrarPonteiros()  # B vira o primeiro e C.proximo passa a apontar para B

    print("\nCaso do unico no:")
    unica = Fila_Circular_Ligada()
    unica.inserir("X")
    print("Com 1 no, ele aponta para ele mesmo:")
    unica.mostrarPonteiros()  # inicio = X | fim = X | fim.proximo = X

    print("Removendo o unico no:")
    unica.remover()
    unica.imprimir()
    unica.mostrarPonteiros()  # inicio = None | fim = None
