from aula06_teoria import ler_nome
from time import sleep
from functools import wraps

def dormir(funcao):
    @wraps(funcao) # faz uma espécie de cópia da função
    def wrapper(*args, **kwargs):
        resultado = funcao(*args, **kwargs) # serve para a "entrada de dados" da função não der erro
        sleep(1)
        return resultado
    return wrapper


class Interruptor:
    def __init__(self, comodo) -> None:
        self.comodo = comodo
    
    def acender(self, pessoa) -> None:
        print(f'{pessoa} foi acender as luzes do cômodo: {self.comodo}')
    
    def apagar(self, pessoa) -> None:
        print(f'{pessoa} foi apagar as luzes do cômodo: {self.comodo}')


class Pessoa: 
    def __init__(self, nome: str) -> None:
        self.nome = nome.capitalize()

    @dormir
    def acender_luzes(self, interruptor: Interruptor) -> None:
        interruptor.acender(self.nome)

    @dormir
    def apagar_luzes(self, interruptor: Interruptor) -> None:
        interruptor.apagar(self.nome)

    @dormir
    def dormir(self) -> None:
        print(f'{self.nome} foi dormir')


interruptor_cozinha = Interruptor('Cozinha')
interruptor_sala = Interruptor('Sala')

nome_pessoa = ler_nome()
pessoa = Pessoa(nome_pessoa)
pessoa.acender_luzes(interruptor_cozinha)
pessoa.apagar_luzes(interruptor_sala)
pessoa.dormir()
