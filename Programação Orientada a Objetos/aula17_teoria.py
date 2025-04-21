from time import sleep

# a teoria fala sobre SOLID (L - Principio de Substituição de Liskov)
class Animal():
    def __init__(self, nome_animal: str):
        self.nome_animal = nome_animal

    def alimentar(self):
        print(f'\033[33m{self.nome_animal} está se alimentando...\033[m')
        sleep(1)


class Cachorro(Animal):
    def latir(self):
        print(f'\033[33mO {self.nome_animal} está latindo...\033[m')
        sleep(1)


class Peixe(Cachorro): # a quebra do principio ocorre aqui
    def nadar(self):
        print('\033[33mO Peixe está nadando...\033[m')
        sleep(1)
    
    def latir(self): # comportamento diferente
        # raise Exception('\033[31mPeixe Não Late!\033[m')
        print('\033[31mPeixe Não Late!\033[m')
        sleep(1)


def verificar_animal(animal: any):
    animal.latir()


obj1 = Animal('Onça')
obj2 = Cachorro('Husky')
obj3 = Peixe('Peixe Dourado')
verificar_animal(obj2)
