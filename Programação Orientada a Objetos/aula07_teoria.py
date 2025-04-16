class MinhaClasse:

    estatico = 'lhama' 
    # tem como declarar váriaveis na classe, desde que esteja fora de algum metódo, mas caso o declare em um só vai funcionar nesse metódo em questão
    
    def __init__(self, estado) -> None:
        self.__estado = estado

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.estatico = 'programador'
obj1.estatico = 'Olá, Mundo!'
MinhaClasse.estatico = 'Lhama Aqui!'

print(obj1.estatico) # lhama
print(obj2.estatico) # lhama
print(MinhaClasse.estatico)
