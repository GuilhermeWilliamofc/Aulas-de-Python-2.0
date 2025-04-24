from time import sleep

# a teoria fala sobre composição

class Selecionar:
    def por_id(self) -> int:
        while True:
            try:
                id = int(input('\033[33mDigite um ID: \033[m'))
            except (ValueError, KeyboardInterrupt):
                print('\033[31mErro: Por favor, Digite um ID válido!\033[m')
                sleep(1)
            else:
                print(f'\033[35mSelecionando o elemento "{id}" no Banco de Dados...\033[m')
                sleep(1)
                return id


class Entrada_de_Dados:
    def digitar_valor(self) -> str:
        valor = ' '
        while valor.isspace() or valor == '' or valor.isnumeric():
            valor = str(input('\033[34mValor: \033[m')).strip().title()
            if valor.isspace() or valor == '' or valor.isnumeric():
                print('\033[31mErro: Por favor, Digite um valor válido!\033[m')
                sleep(1)
        return valor


class Inserir:
    def inserir_valor(self) -> None:
        entrada = Entrada_de_Dados()
        valor = entrada.digitar_valor()
        print(f'\033[36mInserindo o valor "{valor}" no Banco de Dados...\033[m')
        sleep(1)

class Repositorio:
    def __init__(self) -> None:
        self.__selecionar = Selecionar() # composição ocorrendo aqui, pelo oq entendi ao invés de criar fora da classe uma variavel da classe que precisamos para funcionar o código você já coloca ela direto aqui
        self.__inserir = Inserir()

    def selecionar_por_id(self) -> None:
        self.__selecionar.por_id()

    def inserir_valor_no_bd(self) -> None:
        self.__inserir.inserir_valor()

repositorio = Repositorio()
repositorio.selecionar_por_id()
repositorio.inserir_valor_no_bd()
