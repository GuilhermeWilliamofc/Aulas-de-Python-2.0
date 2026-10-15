"""
5. Jogo da batata quente
Os participantes formam uma roda. A cada rodada, a batata passa k vezes para a pessoa seguinte; quem
estiver com ela então é eliminado. Modele a roda com uma fila: cada passe move a pessoa da frente para o fim,
e a eliminação retira a pessoa da frente. Implemente vencedor(participantes, k), que retorna a última pessoa.
Considere k ≥ 0 e uma lista não vazia.
Teste: ["Ana", "Beto", "Caio", "Duda"], k=1 → primeira eliminada "Beto"; vencedora "Ana".
"""

import ex001


def vencedor(participantes, k):
    fila = ex001.Fila()

    for participante in participantes:
        fila.enfileirar(participante)

    while fila.obterQuantidade() > 1:
        for _ in range(k):
            participante = fila.desenfileirar()
            fila.enfileirar(participante)

        fila.desenfileirar()

    return fila.desenfileirar()


if __name__ == "__main__":
    participantes = ["Ana", "Beto", "Caio", "Duda"]
    print(vencedor(participantes, 1))