"""
Recursão é uma técnica onde uma função chama a si mesma para resolver um problema.

Ela é usada principalmente quando um problema pode ser dividido em subproblemas menores do mesmo tipo.
Ao invés de usar laços como for ou while, a recursão resolve os subproblemas repetidamente chamando a própria função.
"""


def fibonacci(cont, num=0, num2=1, contador=0):
    from time import sleep

    soma = num + num2
    if contador != cont:
        print(f"\033[33m{num} + {num2} = {soma}\033[m")
        sleep(1)
        return fibonacci(cont, num2, soma, contador + 1)


print("\033[35mSequência de Fibonacci\033[m")
fibonacci(11)
