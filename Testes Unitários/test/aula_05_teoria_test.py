import pytest
from aula05_teoria import func_de_erro

# a teoria é sobre Testes em Erros

def test_erro():
    try:
        func_de_erro()
    except Exception as erro:
        assert str(erro) == 'Meu Erro está aqui!' # o str() é preciso pq a comparação "==" precisa de dois tipos iguais

def test_erro_com_pytest():
    with pytest.raises(Exception) as info_do_erro:
        func_de_erro()

    assert str(info_do_erro.value) == 'Meu Erro está aqui!'
