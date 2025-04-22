from elementos.interfaces.elemento_interface import ElementoInterface
from time import sleep

class Elemento(ElementoInterface):
    def executar(self) -> None:
        print('\033[36mEstou executando no elemento...\033[m')
        sleep(1)
