class ListaEncadeadaNó:
    def __init__(self, valor, próximo_nó=None):  # o próximo nó começa vazio
        self.valor = valor
        self.próximo_nó = próximo_nó


class ListaEncadeada:
    def __init__(self, cabeça=None):  # a cabeça começa vazia
        self.cabeça = cabeça

    def inserir(self, valor) -> None:
        nó = ListaEncadeadaNó(valor)

        if self.cabeça is None:  # se a lista estiver vazia
            self.cabeça = nó  # a cabeça será igual ao primeiro valor da lista
            return  # esse return ignora todo resto do metodo pois como isso só vai executar para o primeiro valor da lista obviamente não terá outros nós

        nó_atual = self.cabeça  # o nó atual vai ser o primeiro valor da lista

        while True:
            if nó_atual.próximo_nó is None:  # se é o final da lista
                nó_atual.próximo_nó = (
                    nó  # o próximo nó vai ser o último valor que foi inserido na lista
                )
                break
            nó_atual = (
                nó_atual.próximo_nó
            )  # se não for o final, muda o nó atual para o próximo nó

    def printar_lista_encadeada(self):
        nó_atual = self.cabeça  # o nó atual vai ser o primeiro valor da lista
        while nó_atual is not None:  # enquanto não tiver mais valores na lista
            print(nó_atual.valor, "->", end=" ")  # printa o valor atual e uma seta
            nó_atual = nó_atual.próximo_nó  # muda para o próximo nó
        print("None")  # quando o while acabar printa None

    def remover_ultimo_item(self):
        nó_atual = self.cabeça
        while nó_atual.próximo_nó.próximo_nó is not None:
            # percorre a lista até o penúltimo valor
            nó_atual = nó_atual.próximo_nó

        nó_atual.próximo_nó = None
        # o valor após o penúltimo (também conhecido como último) vira None


lista = ListaEncadeada()
lista.printar_lista_encadeada()

lista.inserir(3)
lista.printar_lista_encadeada()

lista.inserir(7)
lista.printar_lista_encadeada()

lista.inserir(10)
lista.printar_lista_encadeada()

lista.inserir(77)
lista.printar_lista_encadeada()

lista.remover_ultimo_item()
lista.printar_lista_encadeada()
