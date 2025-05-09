import aula07_teoria

def desconto_porcento_fake(valor_inicial) -> float:
    return 0.40

def test_calcular_desconto_com_spy_e_retorno_customizado(mocker):
    spy = mocker.patch('aula07_teoria.desconto_porcento', side_effect = desconto_porcento_fake)

    resultado = aula07_teoria.calcular_desconto(100)

    assert resultado == 60.0

    spy.assert_called_once()
    spy.assert_called_with(0.9)

'''
Resumo do script pelo copilot:

Este teste verifica se a função calcular_desconto funciona corretamente ao aplicar um desconto, 
enquanto utiliza um "mock" para substituir a função desconto_porcento. O uso do "mock" permite isolar o teste, 
garantindo que ele não dependa da implementação real de desconto_porcento.

A função desconto_porcento_fake é um "fake" (substituto) que retorna um valor fixo (0.40). 
Ela será usada como um comportamento customizado para substituir a função original desconto_porcento durante o teste.

A função aula07_teoria.desconto_porcento é substituída por um "mock" (espião) que utiliza a função 
desconto_porcento_fake como comportamento. Isso significa que, durante o teste, sempre que desconto_porcento 
for chamada, ela retornará 0.40.
'''
