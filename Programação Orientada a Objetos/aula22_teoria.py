from time import sleep
# a teoria fala sobre Agregação, que no caso geralmente funciona em forma de lista, onde os dados de uma classe, nesse exemplo o carrinho de compras, contém os dados da classe produto


class Produto:
    def __init__(self, nome_produto = str, valor_produto = float) -> None:
        self.__nome_produto: str = nome_produto
        self.__valor_produto: float = valor_produto


    def informacoes_do_produto(self) -> None:
        print(f'\033[36mProduto: \033[33m{self.__nome_produto}\n\033[36mValor: \033[33mR${self.__valor_produto:.2f}\033[m')
        sleep(1)


class Entrada_de_Dados:
    def digitar_nome_produto(self) -> str:
        nome_produto = ' '
        while nome_produto is nome_produto.isspace() or nome_produto.isdigit() or not nome_produto.isalpha():
            nome_produto = str(input('\033[34mNome do Produto: \033[m')).strip().capitalize()
            if nome_produto is nome_produto.isspace() or nome_produto.isdigit() or not nome_produto.isalpha():
                print('\033[31mErro: Por favor, Digite um nome válido!\033[m')
        return nome_produto


    def digitar_valor_produto(self) -> float:
        while True:
            try:
                valor_produto = float(input('\033[34mValor do Produto: \033[m'))
            except (ValueError, KeyboardInterrupt):
                print('\033[31mErro: Por favor, Digite um valor válido!\033[m')
            else:
                break
        return valor_produto


    def deseja_continuar(self) -> str:
        while True:
            resposta = ' '
            while resposta not in 'sn':
                resposta = input('\033[33mDeseja Continuar? [S/N]: \033[m').strip().lower()
                if resposta not in 'sn':
                    print('\033[31mErro: Por favor, Digite somente S ou N!\033[m')
            if resposta in 'sn':
                break
        return resposta


class Carrinho_De_Compras:
    def __init__(self) -> None:
        self.__produtos = []
        self.__entrada_de_dados = Entrada_de_Dados()


    def adicionar_produtos(self) -> None:
        while True:
            entrada = self.__entrada_de_dados
            nome_produto = entrada.digitar_nome_produto()
            valor_produto = entrada.digitar_valor_produto()
            produto = Produto(nome_produto, valor_produto)
            self.__produtos.append(produto)

            resposta = entrada.deseja_continuar()
            if resposta == 'n':
                break


    def finalizar_compra(self) -> None:
        print('\033[32mCompra Finalizada!\033[m')
        sleep(1)
        print('\033[35mLista de Produtos:\033[m')
        for produto in self.__produtos:
            produto.informacoes_do_produto()

carrinho = Carrinho_De_Compras()
carrinho.adicionar_produtos()
carrinho.finalizar_compra()
