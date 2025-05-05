from aula03_teoria import soma_2

# O nome do arquivo precisa ter "_test" no final e é recomendado estar numa pasta chamada test (dentro dela o arquivo de teste e o "__init__.py")

def test_soma2(): #  os nomes das funções devem começar com "test_"
    valor = 5
    resposta = soma_2(valor)
    print(f'{valor} + 2 = {resposta}')
