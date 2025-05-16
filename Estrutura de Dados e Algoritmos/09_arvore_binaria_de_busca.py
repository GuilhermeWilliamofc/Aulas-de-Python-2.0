class ArvoreBinaria:
    def __init__(self, valor: int):
        self.esquerda = None
        self.direita = None
        self.valor = valor
        self.dado = None

    def inserir(self, valor, dado=None):
        if valor < self.valor:
            if self.esquerda is None:
                self.esquerda = ArvoreBinaria(valor)
                self.esquerda.dado = dado
            else:
                self.esquerda.inserir(valor, dado)
        else:
            if self.direita is None:
                self.direita = ArvoreBinaria(valor)
                self.direita.dado = dado
            else:
                self.direita.inserir(valor, dado)

    def caminho_em_ordem(self):  # inorder_traversal
        # reparei que essa função printa a arvore em ordem crescente
        if self.esquerda:
            self.esquerda.caminho_em_ordem()
        print(self.valor)
        if self.direita:
            self.direita.caminho_em_ordem()

    def caminho_pré_ordem(self):  # preorder_traversal
        # reparei que essa função printa a arvore começando pelos galhos da esquerda, quando não tem mais galhos na esquerda, ele começa a printar os galhos da direita
        print(self.valor)
        if self.esquerda:
            self.esquerda.caminho_pré_ordem()
        if self.direita:
            self.direita.caminho_pré_ordem()

    def caminho_pós_ordem(self):  # postorder_traversal
        # reparei que essa função printa a arvore debaixo para cima, começando pelos galhos da esquerda, quando não tem mais galhos na esquerda, ele começa a printar os galhos da direita, tbm debaixo para cima
        if self.esquerda:
            self.esquerda.caminho_pós_ordem()
        if self.direita:
            self.direita.caminho_pós_ordem()
        print(self.valor)

    def procurar(self, valor):
        if valor < self.valor:
            if self.esquerda is None:
                return None
            else:
                return self.esquerda.procurar(valor)
        elif valor > self.valor:
            if self.direita is None:
                return None
            else:
                return self.direita.procurar(valor)
        else:
            return self

    def deletar(self, valor):
        # copilot me ajudo nesse aqui que não consegui fazer sozinho
        if valor < self.valor:
            if self.esquerda:
                self.esquerda = self.esquerda.deletar(valor)
        elif valor > self.valor:
            if self.direita:
                self.direita = self.direita.deletar(valor)
        else:
            # Caso 1: sem filhos - pode ser removido diretamente.
            if self.esquerda is None and self.direita is None:
                return None
            # Caso 2: um filho - substitua o nó pelo seu filho.
            if self.esquerda is None:
                return self.direita
            if self.direita is None:
                return self.esquerda
            # Caso 3: dois filhos - substitua o valor do nó pelo menor valor da subárvore direita (ou maior da esquerda) e remova esse nó substituto.
            sucessor = self.direita
            while sucessor.esquerda:
                sucessor = sucessor.esquerda
            self.valor = sucessor.valor
            self.dado = sucessor.dado
            self.direita = self.direita.deletar(sucessor.valor)
        return self


lista_numeros = [11, 8, 17, 2, 5, 10, 4, 45, 37]
lista_dados = [
    "Abacaxi",
    "Relâmpago",
    "Garfo",
    "Mistério",
    "Camaleão",
    "Horizonte",
    "Túnel",
    "Lâmpada",
    "Brincadeira",
]

arvore = ArvoreBinaria(9)
for numero, dado in zip(lista_numeros, lista_dados):
    arvore.inserir(numero, dado)

print(arvore.procurar(17).dado)
arvore.deletar(45)
arvore.caminho_pré_ordem()
