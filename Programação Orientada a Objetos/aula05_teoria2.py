class MinhaClasse:
    def __init__(self):
        self.__valor = None

    def setter_valor(self, valor: int) -> None:
        self.__valor = valor

    @property # o metódo começa a ser reconhecido como atributo
    def getter_valor(self) -> int:
        return  self.__valor
    
my_class = MinhaClasse()
# my_class.valor = 3 -> Ferindo o encapsulamento

my_class.setter_valor(3)
print(my_class.getter_valor)
