"""
4. Atendimento e reabertura de chamados
Uma equipe de suporte atende chamados na ordem de chegada. Os chamados pendentes ficam em uma fila;
os atendidos ficam em uma pilha, para que o mais recente possa ser reaberto.
Implemente processar_chamados(chamados, operacoes). A operação ATENDER retira o próximo chamado da
fila e o coloca na pilha. A operação REABRIR retira o último chamado atendido da pilha e o coloca no fim da
fila, para ser atendido novamente depois dos demais pendentes. Registre o código movimentado em cada
operação. Considere que as operações fornecidas são válidas.
Teste: com a fila inicial [A, B, C] e as operações ATENDER, ATENDER, REABRIR, ATENDER, os movimentos
são atendeu A, atendeu B, reabriu B, atendeu C. Ao final, B aguarda na fila; C está no topo da pilha
de atendidos.
"""

import ex001


def processar_chamados(chamados, operacoes):
    fila = ex001.Fila()
    pilha = ex001.Pilha()
    movimentos = []

    for chamado in chamados:
        fila.enfileirar(chamado)

    for operacao in operacoes:
        if operacao == "ATENDER":
            chamado = fila.desenfileirar()
            pilha.empilhar(chamado)
            movimentos.append(f"atendeu {chamado}")
        elif operacao == "REABRIR":
            chamado = pilha.desempilhar()
            fila.enfileirar(chamado)
            movimentos.append(f"reabriu {chamado}")

    return movimentos, fila, pilha


if __name__ == "__main__":
    chamados = ["A", "B", "C"]
    operacoes = ["ATENDER", "ATENDER", "REABRIR", "ATENDER"]

    movimentos, fila, pilha = processar_chamados(chamados, operacoes)

    print(movimentos)
    print("Fila:")
    fila.imprimir()
    print("Pilha de atendidos:")
    pilha.imprimir()
