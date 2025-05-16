"""
Hash tables (ou tabelas hash) são estruturas de dados que armazenam pares chave-valor e permitem acesso muito rápido aos dados, geralmente em tempo constante O(1)
O(1), na maioria dos casos.

Em Python, a estrutura de dados que usa hash tables é o dict (dicionário).
"""

from collections import defaultdict

# funciona como um dicionário comum (dict), mas com uma diferença essencial:
# ele cria automaticamente um valor padrão para chaves que ainda não existem, evitando erros do tipo KeyError.

capitais_dict = defaultdict(list)
# defaultdict é uma função que retorna o valor padrão para chaves inexistentes, como int, list, dict, str, etc.

capitais_brasil = ["Brasília", "Rio de Janeiro", "Salvador"]
capitais_dict["Brasil"] += capitais_brasil

capitais_japao = ["Tóquio", "Nara", "Kyoto"]
capitais_dict["Japão"] += capitais_japao

print(dict(capitais_dict))
# print(capitais_dict["Brasil"])

# for capital in capitais_dict["Brasil"]:
#     print(capital)
