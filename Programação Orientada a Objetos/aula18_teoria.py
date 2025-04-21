from abc import ABC, abstractmethod # a biblioteca abc é usada para criar as classes e metodos abstratos
from time import sleep
from random import choice
# a teoria é sobre classes e metodos abstratos

class Pessoa(ABC): # Classe abstrata NÃO possui objetos - só pode ser mãe (herança)
    def correr(self) -> None:
        print('\033[36mA pessoa está correndo...\033[m')
        sleep(1)

    @abstractmethod # Classe filha DEVE criar um metodo trabalhar
    def trabalhar(self):
        pass

class Professor(Pessoa):
    def trabalhar(self) -> None:
        # return super().trabalhar()
        materias = ["Matemática", "Português", "História", "Geografia", "Ciências", "Biologia", "Física", "Química", "Inglês", "Educação Física", "Artes", "Filosofia", "Sociologia", "Redação"]
        escolha = choice(materias)
        print(f'\033[35mO professor está dando aula de {escolha}...\033[m')
        sleep(1)

class Cozinheiro(Pessoa):
    def trabalhar(self) -> None:
        comidas = ["Feijoada", "Lasanha", "Estrogonofe", "Moqueca", "Risoto", "Escondidinho", "Frango assado", "Churrasco", "Sopa de legumes", "Macarronada", "Salada grega", "Camarão ao alho e óleo", "Pizza", "Hambúrguer artesanal", "Torta de frango"]
        escolha = choice(comidas)
        print(f'\033[34mO cozinheiro está preparando {escolha}...\033[m')
        sleep(1)

pessoa1 = Professor()
pessoa1.trabalhar()
pessoa1.correr()

pessoa2 = Cozinheiro()
pessoa2.trabalhar()
