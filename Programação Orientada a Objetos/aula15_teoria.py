from time import sleep
# a teoria é sobre Encapsulamento Protegido, não é realmente protegido, mas é uma convenção para deixar claro para não usar

class Mamifero:
    def __init__(self, localizacao: str, nome_animal: str) -> None:
        self.localizacao = localizacao
        self.nome_animal = nome_animal
        self._tamanho = 1.23

    def andar(self) -> None:
        print(f'\033[33m{self.nome_animal} está andando por {self.localizacao}...\033[m')
        sleep(1)

    def _dormir(self) -> None: 
    # metodo protegido é representado por 1 underline, pode ser usado tanto entre classes por meio da injeção de dependencia ou pela herança e por fora das classes, esse último não é recomendado
        print(f'\033[33m{self.nome_animal} está dormindo...\033[m')

class Gato(Mamifero):
    def __init__(self, localizacao, nome_animal):
        super().__init__(localizacao, nome_animal)

    def miar(self):
        print(f'\033[33mO {self.nome_animal} está miando...\033[m')
        sleep(1)
        self._dormir()
        sleep(1)
        print(self._tamanho)

cat = Gato('Brasil', 'Gato')
cat.miar()
cat._dormir() # Deveria dar erro / elementos protegidos não são chamados por objetos
print(cat._tamanho) # elementos protegidos não são chamados por objetos
