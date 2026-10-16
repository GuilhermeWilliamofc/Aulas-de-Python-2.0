"""
3. Estacionamento de saída única
Em um estacionamento estreito, o último carro que entrou fica mais perto da saída. Implemente
processar_movimentos(comandos) usando uma pilha de placas. ENTRAR placa guarda o carro; SAIR placa
libera o carro somente se ele estiver no topo. Caso contrário, a saída é bloqueada e nada muda. Retorne, na
ordem, "LIBERADA" ou "BLOQUEADA" para cada comando SAIR. Considere placas distintas entre os carros
estacionados.
Teste: ["ENTRAR A", "ENTRAR B", "SAIR A", "SAIR B", "SAIR A"] → ["BLOQUEADA", "LIBERADA",
"LIBERADA"].
"""

import ex001

def processar_movimentos(comando, pilha: ex001.Pilha, placa=""):
    resultado = []

    if comando not in ["ENTRAR", "SAIR"] or placa == "":
        resultado.append("BLOQUEADA")
        return resultado

    if comando == "ENTRAR":
        pilha.empilhar(placa)
        resultado.append("LIBERADA")
    elif comando == "SAIR":
        if pilha.buscar(placa) == 0:
            pilha.desempilhar()
            resultado.append("LIBERADA")
        else:
            resultado.append("BLOQUEADA")

    return resultado

if __name__ == "__main__":
    pilha = ex001.Pilha()
    resultado = []

    comandos = [
        ("ENTRAR", "A"),
        ("ENTRAR", "B"),
        ("SAIR", "A"),
        ("SAIR", "B"),
        ("SAIR", "A")
    ]

    for comando, placa in comandos:
        resultado += processar_movimentos(comando, pilha, placa)

    print(resultado)
