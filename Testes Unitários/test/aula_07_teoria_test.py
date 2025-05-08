import aula07_teoria

# a teoria é sobre Mock Spys (parte 1)

def test_calcular_desconto_com_spy(mocker):
    spy = mocker.spy(aula07_teoria, 'desconto_porcento') # esse tipo de mocker verifica o comportamento de uma função rodando dentro de outra função
    resposta = aula07_teoria.calcular_desconto(100)

    assert resposta == 91.0 # teste de retorno
    spy.assert_called_once() # teste de comportamento
    spy.assert_called_with(0.9)
