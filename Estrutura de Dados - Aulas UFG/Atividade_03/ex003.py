"""
3. Em uma central de atendimento, chegam Ana (prioridade 2), Bruno (1), Carla (2) e Davi (1).
Indique a ordem de atendimento e explique os desempates.

Regra adotada: quanto MENOR o numero, MAIOR a prioridade (1 e mais urgente que 2).
Desempate: quem chegou primeiro e atendido primeiro (FIFO dentro da mesma prioridade).
"""

class No:
    def __init__(self, valor, prioridade, proximo = None):
        self.valor = valor
        self.prioridade = prioridade
        self.proximo = proximo

class Fila_Prioridade:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    def estaVazia(self):
        return self.quantidade == 0

    def obterQuantidade(self):
        return self.quantidade

    def inserir(self, valor, prioridade):
        novo = No(valor, prioridade)

        # se estiver vazia
        if self.estaVazia():
            self.inicio = novo
            self.fim = novo
        # se for mais urgente que o primeiro (prioridade menor), passa na frente de todos
        elif self.inicio is not None and novo.prioridade < self.inicio.prioridade:
            novo.proximo = self.inicio
            self.inicio = novo
        # caso contrario, anda ate o ultimo que tem prioridade <= a do novo
        # (o "<=" eh o desempate: o novo fica DEPOIS de quem ja estava com a mesma prioridade)
        elif self.inicio is not None:
            atual = self.inicio

            while atual.proximo is not None and atual.proximo.prioridade <= novo.prioridade:
                atual = atual.proximo

            novo.proximo = atual.proximo
            atual.proximo = novo

            # se entrou no fim da fila, atualiza o ponteiro fim
            if novo.proximo is None:
                self.fim = novo

        self.quantidade += 1

    def remover(self):
        if self.estaVazia():
            return

        if self.inicio is not None:
            removido = self.inicio
            self.inicio = removido.proximo

            if self.inicio is None:
                self.fim = None

            self.quantidade -= 1
            return removido.valor

    def imprimir(self):
        if self.estaVazia():
            print("Fila Vazia")
            return

        atual = self.inicio

        while atual is not None:
            if atual.proximo is None:
                print(f"{atual.valor}({atual.prioridade})")
                break

            print(f"{atual.valor}({atual.prioridade})", end=", ")
            atual = atual.proximo


if __name__ == "__main__":
    fila = Fila_Prioridade()

    fila.inserir("Ana", 2)
    print("Chegou Ana(2):")
    fila.imprimir()

    fila.inserir("Bruno", 1)
    print("Chegou Bruno(1) -> prioridade menor, passa na frente da Ana:")
    fila.imprimir()

    fila.inserir("Carla", 2)
    print("Chegou Carla(2) -> empata com Ana, chegou depois, fica atras dela:")
    fila.imprimir()

    fila.inserir("Davi", 1)
    print("Chegou Davi(1) -> empata com Bruno, chegou depois, fica atras dele:")
    fila.imprimir()

    print("\nOrdem de atendimento:")
    while not fila.estaVazia():
        print(fila.remover())

    # Resultado: Bruno, Davi, Ana, Carla
    # Desempates:
    # - Bruno x Davi (ambos 1): Bruno chegou antes -> Bruno primeiro
    # - Ana x Carla (ambas 2): Ana chegou antes -> Ana primeiro
