"""
Orientações: resolva em Python 3. Reutilize as classes Pilha e Fila. Acesse as estruturas somente por seus
métodos públicos, sem manipular os nós internos. Teste também estruturas vazias quando couber.
1. Mesmas entradas, saídas diferentes
Crie uma pilha e uma fila vazias. Em cada uma, adicione 10, 20 e 30, nessa ordem; retire um elemento;
adicione 40; retire mais dois. Imprima a sequência de retiradas e os elementos restantes em cada estrutura.
Explique a diferença entre as duas saídas.
Use empilhar/desempilhar e enfileirar/desenfileirar.
"""

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
            print(f'{atual.valor} ', end="")
            atual = atual.proximo
        print()

    def buscar(self, valor):
        if self.estaVazia():
            return None

        atual = self.inicio
        contador = 0

        while atual is not None:
            if atual.valor == valor:
                return contador
            atual = atual.proximo
            contador += 1

        return None

    def liberar(self):
        self.inicio = None
        self.quantidade = 0

class Fila(Lista):
    def __init__(self):
        self.inicio = None
        self.quantidade = 0

    def enfileirar(self, valor):
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

    def desenfileirar(self):
        if self.estaVazia():
            return 0

        atual = self.inicio
        if atual is not None:
            valor = atual.valor
            self.inicio = atual.proximo
            self.quantidade -= 1
            return valor

class Pilha(Lista):
    def __init__(self):
        self.inicio = None
        self.quantidade = 0

    def empilhar(self, valor):
        inicio = self.inicio
        novo = No(valor)

        novo.proximo = inicio
        self.inicio = novo

        self.quantidade += 1
        return 1

    def desempilhar(self):
        if self.estaVazia():
            return 0

        atual = self.inicio
        if atual is not None:
            valor = atual.valor
            self.inicio = atual.proximo
            self.quantidade -= 1
            return valor

if __name__ == "__main__":
    pilha = Pilha()
    fila = Fila()

    print("Pilha:")
    pilha.empilhar(10)
    pilha.imprimir()
    pilha.empilhar(20)
    pilha.imprimir()
    pilha.empilhar(30)
    pilha.imprimir()

    print("Fila:")
    fila.enfileirar(10)
    fila.imprimir()
    fila.enfileirar(20)
    fila.imprimir()
    fila.enfileirar(30)
    fila.imprimir()

    print("Pilha:")
    pilha.desempilhar()
    pilha.imprimir()

    print("Fila:")
    fila.desenfileirar()
    fila.imprimir()

    print("Pilha:")
    pilha.empilhar(40)
    pilha.imprimir()
    print("Fila:")
    fila.enfileirar(40)
    fila.imprimir()

    print("Pilha:")
    pilha.desempilhar()
    pilha.desempilhar()
    pilha.imprimir()

    print("Fila:")
    fila.desenfileirar()
    fila.desenfileirar()
    fila.imprimir()