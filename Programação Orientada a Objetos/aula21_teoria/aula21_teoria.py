from time import sleep
from elementos.interfaces.elemento_interface import ElementoInterface
from elementos.elemento2 import Elemento2

# a teoria é sobre SOLID - (D) - Inversão da Dependência


class Principal:
    def __init__(self, elem: ElementoInterface): # pelo oq entendi vc cria uma interface da classe Elemento para que a classe Principal não seja 100% dependente da classe Elemento caso ela precise ser refeita, já que a interface serve como um "template" e impede em partes que a classe tenha mudanças de nome de metodos prejudicando assim a estrutura do codigo da classe principal
        self.__elem = elem

    def run(self) -> None:
        self.__elem.executar()
        print('\033[35mEstou finalizando na classe principal...\033[m')
        sleep(1)

elem = Elemento2()

cl1 = Principal(elem)
cl1.run()
