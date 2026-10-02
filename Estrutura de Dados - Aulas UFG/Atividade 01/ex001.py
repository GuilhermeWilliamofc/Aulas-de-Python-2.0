class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo: No | None = None

class Lista:
    # inicio recebe ou No ou None, se nenhum valor for declarado entao self.inicio recebe None
    def __init__(self):
        self.inicio = None
        self.quantidade = 0

    def estaVazia(self):
        if (self.inicio is None):
            return 1
        
        return 0

    def obterQuantidade(self):
        return self.quantidade

    def imprimir(self):
        if self.estaVazia():
            print('')
            return

        atual = self.inicio

        while atual is not None:
            print(f'{atual.valor}')
            atual = atual.proximo

    def inserirInicio(self, valor):
        inicio = self.inicio
        novo = No(valor)

        novo.proximo = inicio
        self.inicio = novo

        self.quantidade += 1
        return 1

    def inserirFinal(self, valor):
        novo = No(valor)

        if self.inicio is None:
            self.inicio = novo
            self.quantidade += 1
            return 1

        atual = self.inicio

        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo
        self.quantidade += 1
        return 1

    def buscar(self, valor):
        if self.estaVazia():
            return 0

        atual = self.inicio

        while atual is not None:
            if atual.valor == valor:
                return 1
            atual = atual.proximo

        return 0

    def remover(self, valor):
        if self.estaVazia():
            return 0

        atual = self.inicio

        if atual is not None and atual.valor == valor:
            self.inicio = atual.proximo
            self.quantidade -= 1
            return 1

        anterior = atual

        if atual is not None:
            atual = atual.proximo

        while atual is not None and anterior is not None:
            if atual.valor == valor:
                anterior.proximo = atual.proximo
                self.quantidade -= 1
                return 1
            anterior = atual
            atual = atual.proximo

        return 0

    def liberar(self):
        self.inicio = None
        self.quantidade = 0