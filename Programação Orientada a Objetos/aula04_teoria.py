class Pessoa:
    def __init__(self, altura, cpf):
        self.altura = altura
        # os dois underlines determinam atributos e metodos privados (não podem ser executados fora da classe)
        self.__cpf = cpf

    def apresentar(self):
        print(f'Olá! Minha altura - {self.altura}m')
        self.__coletar_documento()

    def __coletar_documento(self):
        print(f'Meu documento - {self.__cpf}')

jorge = Pessoa('1.70', '123.456.789-00')
jorge.apresentar()
