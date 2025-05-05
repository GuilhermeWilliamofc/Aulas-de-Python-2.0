from aula04_teoria import divisao_2, informacoes
from random import randint # não tem na teoria mas quis testar valores aleatórios

def test_divisao_2():
    valor = randint(0, 100)
    resposta = divisao_2(valor)
    print(f'{valor} / 2 = {resposta}')
    resposta2 = divisao_2(8)
    print(f'8 / 2 = {resposta2}')

    assert resposta2 == 4 # assert pode ser interpretado como "é verdade que..."
    assert isinstance(resposta, float) # checa se a resposta é um float
    assert isinstance(resposta2, float)

def test_informacoes():
    resposta = informacoes()
    
    assert isinstance(resposta, dict) # checa se a resposta é um dicionário
    assert 'nome' in resposta
    assert 'altura' not in resposta
    assert 'Gui' in resposta['nome']
    assert resposta['tá_ok'] # checando True ou False (se for False dá erro)
