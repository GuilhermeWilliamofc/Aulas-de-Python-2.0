# recursão = uma função que chama a si mesma internamente

# ajuda a visualizar um problema complexo em etapas básicas
# problemas podem ser resolvidos mais facilmente de forma iterativa ou recursiva

# iterativo = mais rápido, mais complexo
# recursivo = mais lento, mais simples


# iterativo
def andar(passos):
    for passo in range(1, passos + 1):
        print(f"Você andou {passo} passos")


def fatorial(x):
    resultado = 1
    if x > 0:
        for y in range(1, x + 1):
            resultado *= y
        return resultado


# recursivo
def andar2(passos):
    if passos == 0:
        return
    andar(passos - 1)
    print(f"Você andou {passos} passos")


def fatorial2(x):
    if x == 1:
        return 1
    else:
        return x * fatorial2(x - 1)


print(fatorial2(5))
