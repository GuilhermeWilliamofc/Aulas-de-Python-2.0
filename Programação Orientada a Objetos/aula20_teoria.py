from abc import ABC, abstractmethod
from random import choice
from time import sleep

# a teoria é sobre SOLID - (I) - Segregação das Interfaces


class Trabalhador(ABC): # a segragação é quando quero usar a interface mas não quero usar todos os metodos abstratos, somente alguns
    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass

    @abstractmethod
    def consultar_beneficios(self) -> None:
        pass

class Trabalhador_Temporario(ABC): # então devemos criar uma copia da interface sem os metodos abstratos que não vamos usar
    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        materias = ["Matemática", "Português", "História", "Geografia", "Ciências", "Biologia", "Física", "Química", "Inglês", "Educação Física", "Artes", "Filosofia", "Sociologia", "Redação"]
        escolha = choice(materias)
        print(f'\033[33mO professor está dando aula de {escolha}...\033[m')
        sleep(1)

    def ir_para_casa(self) -> None:
        meio_de_transporte = ["carro", "ônibus", "metrô", "moto", "bicicleta", "táxi", "uber", "a pé"]
        escolha = choice(meio_de_transporte)
        print(f'\033[35mO professor foi para casa de {escolha}\033[m')
        sleep(1)

    def consultar_beneficios(self):
        print('\033[33mConsultando beneficios da CLT...\033[m')
        sleep(1)

class Professor_Substituto(Trabalhador_Temporario): # usamos a interface segregada
    def trabalhar(self) -> None:
        materias = ["Matemática", "Português", "História", "Geografia", "Ciências", "Biologia", "Física", "Química", "Inglês", "Educação Física", "Artes", "Filosofia", "Sociologia", "Redação"]
        escolha = choice(materias)
        print(f'\033[33mO professor está dando aula de {escolha}...\033[m')
        sleep(1)

    def ir_para_casa(self) -> None:
        meio_de_transporte = ["carro", "ônibus", "metrô", "moto", "bicicleta", "táxi", "uber", "a pé"]
        escolha = choice(meio_de_transporte)
        print(f'\033[36mO professor foi para casa de {escolha}\033[m')
        sleep(1)

pessoa2 = Professor_Substituto()
pessoa2.trabalhar()
pessoa2.ir_para_casa()
