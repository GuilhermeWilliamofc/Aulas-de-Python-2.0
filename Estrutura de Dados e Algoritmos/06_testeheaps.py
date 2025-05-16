import heapq
from time import sleep

pessoas = [
    (25, "Ana"),
    (30, "Bruno"),
    (18, "Carlos"),
    (40, "Daniela"),
    (35, "Vinicius"),
]
pessoas = [(-idade, nome) for idade, nome in pessoas]
# transformando todas as idades em números negativos para fazer o max-heap
heapq.heapify(pessoas)

while pessoas:  # pode ser traduzido como: enquanto tiver pessoas na lista
    # o certo é usar while aqui ao invés de for, pois no for ele vai percorrer a lista toda e a ordem vai estar ""bagunçada"" pela estrutura que o heap tem
    idade, nome = heapq.heappop(pessoas)  # apaga a pessoa mais nova da lista (min-heap)
    print(f"\033[33mAtendendo {nome} (idade: {-idade})\033[m")
    sleep(1)

print("\033[32mTodos os Clientes foram atendidos!\033[m")
