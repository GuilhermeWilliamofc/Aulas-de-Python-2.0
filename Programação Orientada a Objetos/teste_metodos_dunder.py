# Metodos Dunder/Metodos Mágicos - Dunder (Abreviação para double underscore) exemplos: __init__, __str__, __eq__, etc
#                                  Eles são automaticamente chamados em muitas operações internas do python (como criar um objeto, imprimir, comparar, somar, acessar índice etc).
#                                  Elas servem para os devs definirem e customizarem o comportamento dos objetos


class Livro:
    def __init__(self, titulo: str, autor: str, num_paginas: int):
        # init é um metodo dunder
        # → Construtor
        # Chamado automaticamente quando você cria um objeto.
        # Serve para: inicializar atributos do objeto.

        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def __str__(self):
        # Chamado quando você usa print(objeto) ou str(objeto).
        # Caso não seja utilizada ao utilizar o print ou str aparecerá algo como "<__main__.Livro object at 0x000002A39A9170E0>"
        return f'"{self.titulo}" de {self.autor}'

    def __eq__(self, outro_livro):
        # → relacionado a Igualdade (==), "eq" vem de equal do inglês
        # Chamado quando você usa obj1 == obj2.
        # Serve para: definir como dois objetos são considerados iguais.
        return self.titulo == outro_livro.titulo or self.autor == outro_livro.autor
        # vai retornar um valor booleano (True ou False)

    def __lt__(self, outro_livro):
        # -> lt vem do inglês (less than), Chamado quando você faz: obj1 < obj2
        # Serve para: definir o que significa "menor que" entre dois objetos.
        return self.num_paginas < outro_livro.num_paginas
        # também retorna booleano

    def __gt__(self, outro_livro):
        # -> gt vem do inglês (Greater Than), Chamado quando você faz: obj1 > obj2
        # Serve para: definir o que significa "maior que".
        return self.num_paginas > outro_livro.num_paginas

    def __add__(self, outro_livro):
        # → Soma (obj1 + obj2)
        # Você pode definir como objetos são somados.
        return f'"{self.titulo}" + "{outro_livro.titulo}" = {self.num_paginas + outro_livro.num_paginas} páginas'

    def __contains__(self, palavra_procurada):
        # Esse método é chamado quando você usa o operador in
        return palavra_procurada in self.titulo or palavra_procurada in self.autor
        # retorna booleano

    def __getitem__(self, atributo_procurado):
        # → Acesso por índice ou chave (obj[chave])
        # Chamado quando se usa colchetes.
        # Serve para: permitir que objetos sejam acessados como listas ou dicionários.
        if atributo_procurado == "titulo":
            return self.titulo
        elif atributo_procurado == "autor":
            return self.autor
        elif atributo_procurado == "num_paginas":
            return self.num_paginas
        else:
            return (
                f'\033[31mO atributo "{atributo_procurado}" não foi encontrado!\033[m'
            )


livro1 = Livro("1984", "George Orwell", 312)
livro2 = Livro("The Hobbit", "J.R.R. Tolkien", 310)
livro3 = Livro("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
livro4 = Livro("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
print(livro1)

print(livro1 == livro2)  # utilizando o __eq__
print(livro2 < livro3)  # utilizando o __lt__
print(livro4 > livro1)  # utilizando o __gt__
print(livro2 + livro4)  # utilizando o __add__
print("George" in livro1)  # utilizando o __contains__
print(livro3["autor"])  # utilizando o __getitem__
