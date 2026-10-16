"""
6. Inversão de uma pilha com uma fila
Uma pilha de tarefas precisa ser executada na ordem oposta à atual. Implemente inverter_pilha(pilha) com uma
fila auxiliar: transfira os itens da pilha para a fila e depois devolva-os à mesma pilha. Use apenas empilhar,
desempilhar, enfileirar, desenfileirar e esta_vazia. A fila auxiliar deve terminar vazia.
Teste: pilha com topo 30, 20, 10 → novo topo 10, 20, 30. Inclua pilha vazia e com um item.
"""

import ex001


def inverter_pilha(pilha):
    fila = ex001.Fila()

    while pilha.estaVazia() == 0:
        fila.enfileirar(pilha.desempilhar())

    while fila.estaVazia() == 0:
        pilha.empilhar(fila.desenfileirar())

    return pilha


if __name__ == "__main__":
    pilha = ex001.Pilha()
    pilha.empilhar(10)
    pilha.empilhar(20)
    pilha.empilhar(30)

    # antes
    print("Antes")
    pilha.imprimir()

    inverter_pilha(pilha)

    # depois
    print("Depois")
    pilha.imprimir()