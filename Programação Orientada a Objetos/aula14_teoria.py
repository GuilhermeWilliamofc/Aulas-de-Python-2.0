from time import sleep
# a teoria é sobre herança

class Mamifero:
    def __init__(self, localizacao: str, nome_animal: str) -> None:
        self.localizacao = localizacao
        self.nome_animal = nome_animal

    def andar(self) -> None:
        print(f'\033[33m{self.nome_animal} está andando por {self.localizacao}...\033[m')
        sleep(1)

class Cachorro(Mamifero): # a classe cachorro herda todos os metodos da classe mamifero
    def __init__(self, localizacao, nome_animal):
        super().__init__(localizacao, nome_animal)

    def latir(self):
        print(f'\033[33mO {self.nome_animal} está latindo...\033[m')
        sleep(1)
        self.andar()
    
class Gato(Mamifero):
    def __init__(self, localizacao, nome_animal):
        super().__init__(localizacao, nome_animal)

    def miar(self):
        print(f'\033[33mO {self.nome_animal} está miando...\033[m')

cachorro = Cachorro('São Paulo', 'Pastor Alemão')
gato = Gato('Goiânia', 'Gato')

cachorro.latir()
gato.miar()
