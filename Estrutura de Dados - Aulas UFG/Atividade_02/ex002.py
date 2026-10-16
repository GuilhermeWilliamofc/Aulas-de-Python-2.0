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
pares = {"}": "{", "]": "[", ")": "("}
aberturas = set(pares.values())

balanceado = True

for caractere in teste:
    if caractere in aberturas:
        pilha.empilhar(caractere)
    elif caractere in pares:
        if pilha.buscar(pares[caractere]) != 0:
            balanceado = False
            break
        pilha.desempilhar()

if pilha.obterQuantidade() > 0:
    balanceado = False

print(balanceado)
