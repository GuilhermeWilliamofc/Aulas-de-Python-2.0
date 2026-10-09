"""
2. Delimitadores de um trecho de código
Um editor deve conferir se parênteses (), colchetes [] e chaves {} aparecem em pares e na ordem correta.
Implemente balanceado(texto) com uma pilha: cada símbolo de fechamento deve corresponder ao último
símbolo de abertura ainda não fechado. Ignore letras e operadores. Retorne True ou False.
Teste: "{a+[b*(c-d)]}" → True; "([)]" → False; "(()" → False; "]" → False.
"""

import ex001

teste = "{a+[b*(c-d)]}"
pilha = ex001.Pilha()

for caractere in teste:
    if caractere in ["{", "[", "("]:
        pilha.empilhar(caractere)
        pilha.imprimir()
    elif caractere in ["}", "]", ")"]:
        if caractere == "}":
            if pilha.buscar("{") == 0:
                pilha.desempilhar()
                pilha.imprimir()
        elif caractere == "]":
            if pilha.buscar("[") == 0:
                pilha.desempilhar()
                pilha.imprimir()
        elif caractere == ")":
            if pilha.buscar("(") == 0:
                pilha.desempilhar()
                pilha.imprimir()

pilha.imprimir()