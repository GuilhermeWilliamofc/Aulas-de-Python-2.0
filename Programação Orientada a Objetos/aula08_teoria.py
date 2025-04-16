class MinhaClasse:

    estatico = 'lhama' 
    
    def __init__(self, estado) -> None:
        self.__estado = estado

    def print_variavel_de_classe(self):
        print(self.estatico)

    @classmethod
    def alteracao_de_variavel_de_classe(cls):
        cls.estatico = 'alguma coisa'
        # similar ao resultado de MinhaClasse.estatico = 'alguma coisa'
        # muda o valor estatico de 'lhama' para 'alguma coisa' sem espelhar

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

obj1.alteracao_de_variavel_de_classe() # se remover essa linha o valor muda para default (lhama)

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico) # o metódo muda a variável 'globalmente'
