from abc import ABC, abstractmethod
from random import choice
from time import sleep

# a teoria é sobre interface


class Trabalhador(ABC): # interface é uma classe abstrata com TODOS os metodos abstratos
    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def horario_de_almoco(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass


class Engenheiro(Trabalhador):
    def trabalhar(self) -> None:
        atividades = ["Analisando solo para fundação", "Supervisionando concretagem", "Verificando alinhamento de pilares", "Calculando carga estrutural", "Inspecionando armadura de ferro", "Coordenando equipe de obra", "Elaborando cronograma físico-financeiro", "Fazendo levantamento topográfico", "Revisando planta estrutural", "Avaliando materiais de construção"]
        escolha = choice(atividades)
        print(f'\033[33mO engenheiro está {escolha}...\033[m')
        sleep(1)

    def horario_de_almoco(self) -> None:
        almoço = ["Feijoada", "Lasanha de berinjela", "Estrogonofe de frango", "Moqueca de peixe", "Risoto de camarão",
    "Escondidinho de carne seca", "Frango grelhado com legumes", "Churrasco com mandioca", "Sopa de ervilha",
    "Macarrão à bolonhesa", "Salada completa com grão-de-bico", "Camarão ao alho e óleo", "Pizza marguerita",
    "Hambúrguer artesanal", "Torta de frango com salada", "Arroz, feijão, bife acebolado e batata frita",
    "Yakissoba", "Filé de salmão com purê", "Panqueca de carne moída", "Esfirra de carne com limão"
]
        escolha = choice(almoço)
        print(f'\033[36mO engenheiro está almoçando {escolha}...\033[m')
        sleep(1)

    def ir_para_casa(self) -> None:
        meio_de_transporte = ["carro", "ônibus", "metrô", "moto", "bicicleta", "táxi", "uber", "a pé"]
        escolha = choice(meio_de_transporte)
        print(f'\033[35mO engenheiro foi para casa de {escolha}\033[m')
        sleep(1)


class Medico(Trabalhador):
    def trabalhar(self) -> None:
        atividades = ["Realizando consulta", "Fazendo cirurgia", "Prescrevendo remédio", "Analisando exames", "Atendendo emergência", "Verificando sinais vitais", "Aplicando vacina", "Fazendo diagnóstico", "Acompanhando paciente no pós-operatório", "Explicando tratamento ao paciente"]
        escolha = choice(atividades)
        print(f'\033[33mO médico está {escolha}...\033[m')
        sleep(1)

    def horario_de_almoco(self) -> None:
        almoço = ["Feijoada", "Lasanha de berinjela", "Estrogonofe de frango", "Moqueca de peixe", "Risoto de camarão",
    "Escondidinho de carne seca", "Frango grelhado com legumes", "Churrasco com mandioca", "Sopa de ervilha",
    "Macarrão à bolonhesa", "Salada completa com grão-de-bico", "Camarão ao alho e óleo", "Pizza marguerita",
    "Hambúrguer artesanal", "Torta de frango com salada", "Arroz, feijão, bife acebolado e batata frita",
    "Yakissoba", "Filé de salmão com purê", "Panqueca de carne moída", "Esfirra de carne com limão"
]
        escolha = choice(almoço)
        print(f'\033[36mO médico está almoçando {escolha}...\033[m')
        sleep(1)

    def ir_para_casa(self) -> None:
        meio_de_transporte = ["carro", "ônibus", "metrô", "moto", "bicicleta", "táxi", "uber", "a pé"]
        escolha = choice(meio_de_transporte)
        print(f'\033[35mO médico foi para casa de {escolha}\033[m')
        sleep(1)


def rotina_trabalhador(trabalhador: Trabalhador): # em interfaces você pode usar o nome da classe mãe para usar as classes filhas (não tenho certeza se é exclusivo de interfaces)
    trabalhador.trabalhar()
    trabalhador.horario_de_almoco()
    print('\033[32mComunicar o trabalhador para ir para casa\033[m')
    sleep(1)
    trabalhador.ir_para_casa()

pessoa1 = Medico()
pessoa2 = Engenheiro()

rotina_trabalhador(pessoa1)
print()
rotina_trabalhador(pessoa2)
