"""
1. No deque, insira 10 no início, 20 no fim e 5 no início. Retire uma vez de cada extremidade. Quais
valores saem e qual permanece? Repita partindo de um deque vazio e com um único item.
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


if __name__ == "__main__":
    deque = Deque()
    deque.inserirInicio(10)
    deque.inserirFinal(20)
    deque.inserirInicio(5)

    print("Deque Completo:")
    deque.imprimir()
    print("Removendo no Inicio:")
    deque.removerInicio()
    deque.imprimir()
    print("Removendo no Final:")
    deque.removerFinal()
    deque.imprimir()
    print("Removendo no Inicio:")
    deque.removerInicio()
    deque.imprimir()

    print("\nTeste partindo de um Deque Vazio")
    deque_vazio = Deque()
    print("Deque Completo:")
    deque_vazio.imprimir()
    print("Removendo no Final:")
    deque_vazio.removerFinal()
    deque_vazio.imprimir()
    print("Removendo no Inicio:")
    deque_vazio.removerInicio()
    deque_vazio.imprimir()

    print("\nTeste partindo de um Deque Com 1 Elemento")
    deque_unitario = Deque()
    deque_unitario.inserirInicio(67)
    print("Deque Completo:")
    deque_unitario.imprimir()
    print("Removendo no Final:")
    deque_unitario.removerFinal()
    deque_unitario.imprimir()
    print("Removendo no Inicio:")
    deque_unitario.removerInicio()
    deque_unitario.imprimir()