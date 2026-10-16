"""
2. Em uma fila circular de capacidade 4, insira A, B e C; retire A e B; insira D, E, F e G. Em que
operação ocorre falha? Escreva o índice de início e a ordem lógica antes da falha.
"""

class No:
    def __init__(self, valor, anterior = None, proximo = None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

class Deque:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    def estaVazia(self):
        return self.quantidade == 0

    def obterQuantidade(self):
        return self.quantidade

    def inserirInicio(self, valor):
        novo = No(valor)

        # se estiver vazia
        if self.estaVazia():
            self.inicio = novo
            self.fim = novo
        # se estiver com pelo menos 1 elemento
        elif self.inicio is not None:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

        self.quantidade += 1

    def inserirFinal(self, valor):
        novo = No(valor)

        # se estiver vazia
        if self.estaVazia():
            self.inicio = novo
            self.fim = novo
        # se estiver com pelo menos 1 elemento
        elif self.fim is not None:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

        self.quantidade += 1

    def removerInicio(self):
        if self.estaVazia():
            return

        if self.inicio is not None:
            removido = self.inicio
            novo_inicio = self.inicio.proximo
            self.inicio = novo_inicio

            if novo_inicio is None:
                self.fim = None
            else:
                novo_inicio.anterior = None

            self.quantidade -= 1
            return removido.valor

    def removerFinal(self):
        if self.estaVazia():
            return

        if self.fim is not None:
            removido = self.fim
            novo_fim = self.fim.anterior
            self.fim = novo_fim

            if novo_fim is None:
                self.inicio = None
            else:
                novo_fim.proximo = None

            self.quantidade -= 1
            return removido.valor

    def imprimir(self):
        if self.estaVazia():
            print("Deque Vazio")
            return

        atual = self.inicio

        while atual is not None:
            if atual.proximo is None:
                print(f"{atual.valor}")
                atual = atual.proximo
                break

            print(f"{atual.valor}", end=", ")
            atual = atual.proximo