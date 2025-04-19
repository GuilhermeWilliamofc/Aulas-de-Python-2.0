# a teoria fala sobre SOLID (O) - Princípio Aberto / Fechado, que consiste em fazer uma função, classe, etc sem precisar ficar modificando a mesma toda vez que for adicionar uma nova funcionalidade na classe ou algo do tipo

class Artista:
    def __init__(self, tipo: str):
        self.tipo = tipo

    def apresentar_show(self) -> None:
        print(f'O {self.tipo} está apresentando seu show!')

class Circo:
    def apresentar(self, artista: Artista) -> None:
        print('O circo está abrindo!')
        artista.apresentar_show()
        print('O público aplaude!')

circo = Circo()
palhaço = Artista('palhaço')
magico = Artista('mágico')
malabarista = Artista('malabarista')

circo.apresentar(magico)
