from aula06_teoria import calcular_desconto

# a teoria é sobre Introdução aos Mocks

def test_calcular_desconto(mocker): # o mock substitui a função desconto_porcento (Ele é usado para substituir temporariamente funções, métodos, objetos ou comportamentos durante os testes, permitindo isolar o que está sendo testado.)
    mocker.patch('aula06_teoria.desconto_porcento', return_value = 0.50)

    resposta = calcular_desconto(100)

    assert resposta == 50
