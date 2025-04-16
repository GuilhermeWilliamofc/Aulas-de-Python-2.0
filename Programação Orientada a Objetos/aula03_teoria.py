class MinhaClasse:
    def __init__(self, info, elem): # metodo construtor é o primeiro a rodar
        self.atributo1 = 'meu atributo'
        self.atributo2 = elem
        self.atributo3 = [1, 2, 'a']
        self.atributo_novo = info
        print(self.atributo_novo)
    
    def metodo_1(self):
        print('minha ação 1')
        print('minha ação 2')
        print(self.atributo2)
        return 'Olá, Mundo'
    
    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo3[1] + numero)
    
# objeto       # classe -> instanciamos um objeto
minha_classe = MinhaClasse('info aqui no construtor', 213)

# response = minha_classe.metodo_1()
# print(response)

minha_classe.metodo_2(3)
