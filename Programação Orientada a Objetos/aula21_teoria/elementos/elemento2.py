from elementos.interfaces.elemento_interface import ElementoInterface
from time import sleep

class Elemento2(ElementoInterface):
    def executar(self) -> None:
        print('\033[33mEstou executando no elemento alternativo...\033[m')
        sleep(1)
