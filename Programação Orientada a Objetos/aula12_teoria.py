from time import sleep
from random import choice

class Celular:
    def __init__(self, marca: str) -> None:
        self.marca = marca

    def enviar_mensagem(self, mensagem: str) -> None:
        print(f'\033[36mEnviando mensagem: "{mensagem}"\033[m')
        sleep(1)
        print('\033[32mMensagem enviada!\033[m')

    def abrir_emails(self) -> None:
        print('\033[33mAbrindo email...\033[m')
        sleep(1)
        print('\033[32mEmail aberto!\033[m')
        sleep(1)

    def abrir_youtube(self) -> None:
        print('\033[31mAbrindo Youtube...\033[m')
        sleep(1)
        print('\033[32mYoutube aberto!\033[m')


class Pessoa:
    def __init__(self, celular: Celular):
        self.__celular = celular # deixa privado e gera a depedência com a classe Celular

    def pedir_pizza(self) -> None:
        sabores = ["Margherita", "Calabresa", "Portuguesa", "Frango com Catupiry", "Quatro Queijos", "Pepperoni", "Muçarela", "Napolitana", "Atum", "Vegetariana", "Bacon", "Palmito", "Carne Seca com Catupiry", "Lombo com Requeijão", "Brócolis com Bacon", "Chocolate", "Prestígio", "Romeu e Julieta", "Banana com Canela"]
        escolha = choice(sabores)
        print('\033[33mBuscando o celular...\033[m')
        sleep(1)
        print('\033[35mDefinindo o sabor...\033[m')
        sleep(1)
        self.__celular.enviar_mensagem(f'Quero uma de {escolha}!')
        sleep(1)

    def estudar(self) -> None:
        print('\033[33mSentando no computador...\033[m')
        sleep(1)
        self.__celular.abrir_youtube()
        sleep(1)
        print('\033[36mAnotando o conteúdo...\033[m')
        sleep(1)

android = Celular('motorola')
ios = Celular('iphone')

joão = Pessoa(android)
ana = Pessoa(ios)

joão.pedir_pizza()
print()
ana.estudar()
