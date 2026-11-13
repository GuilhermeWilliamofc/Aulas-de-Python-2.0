"""
2. Em uma fila circular de capacidade 4, insira A, B e C; retire A e B; insira D, E, F e G. Em que
operação ocorre falha? Escreva o índice de início e a ordem lógica antes da falha.
"""

class No:
    def __init__(self, valor, anterior = None, proximo = None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

class Fila_Circular:
    def __init__(self, capacidade = 4):
        self.inicio = None
        self.fim = None
        self.quantidade = 0
        self.capacidade = capacidade

    def estaVazia(self):
        return self.quantidade == 0

    def obterQuantidade(self):
        return self.quantidade

    def inserir(self, valor):
        if self.quantidade == self.capacidade:
            return
        
        novo = No(valor)

        # se estiver vazia
        if self.estaVazia():
            self.inicio = novo
            self.fim = novo
            self.fim.proximo = self.inicio
            self.inicio.anterior = self.fim
        # se estiver com pelo menos 1 elemento
        elif self.fim is not None and self.inicio is not None:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo
            self.fim.proximo = self.inicio
            self.inicio.anterior = self.fim

        self.quantidade += 1

    def remover(self, valor):
        if self.estaVazia() or self.inicio is None:
            return False

        atual = self.inicio

        for i in range(self.quantidade):

            if atual is None:
                return False

            if atual.valor == valor:

                # Se existir apenas um elemento
                if self.quantidade == 1:
                    self.inicio = None
                    self.fim = None

                # Se for o primeiro
                elif atual == self.inicio:
                    if atual.proximo is None or self.fim is None:
                        return False

                    self.inicio = atual.proximo
                    self.inicio.anterior = self.fim
                    self.fim.proximo = self.inicio

                # Se for o último
                elif atual == self.fim:
                    if atual.anterior is None or self.inicio is None:
                        return False

                    self.fim = atual.anterior
                    self.fim.proximo = self.inicio
                    self.inicio.anterior = self.fim

                # Se estiver no meio
                else:
                    if atual.anterior is None or atual.proximo is None:
                        return False

                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior

                self.quantidade -= 1
                return True

            atual = atual.proximo

        return False

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

if __name__ == "__main__":
    fila = Fila_Circular()
    fila.inserir("A")
    fila.inserir("B")
    fila.inserir("C")
    fila.imprimir()

    fila.remover("A")
    fila.remover("B")
    fila.imprimir()

    fila.inserir("D")
    fila.inserir("E")
    fila.inserir("F")
    fila.inserir("G") # "G" nao eh inserido
    fila.imprimir()