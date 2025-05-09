import pickle
from time import sleep


class Arquivo:
    """Essa classe gerencia arquivos .pkl"""

    def carregar_lista(self) -> list:
        """Carrega um arquivo .pkl de uma lista de filmes

        Retorna:
            list: caso exista o arquivo da lista, ela vai ser retornada
        """

        try:
            with open("lista_filmes.pkl", "rb") as arquivo:
                lista_filmes = pickle.load(arquivo)
        except Exception as erro:
            print(f"\033[31mErro ({erro}): Erro durante o Carregamento da Lista!\033[m")
            return []
        else:
            print("\033[32mLista carregada com sucesso!\033[m")
            return lista_filmes

    def salvar_lista(self, lista: list):
        """Salva a lista de filmes em um arquivo .pkl

        Argumentos:
            lista (list): lista de filmes
        """
        with open("lista_filmes.pkl", "wb") as arquivo:
            pickle.dump(lista, arquivo)


class Input_de_Dados:
    """Essa classe gerencia a entrada de dados"""

    def opcoes(self) -> int:
        """Mostra um menu com opções para o usuário escolher

        Retorna:
            int: a opção escolhida pelo usuário
        """
        while True:
            print("\033[33m[ 1 ] - Adicionar Filme")
            print("[ 2 ] - Ver Lista de Filmes")
            print("[ 3 ] - Sair do Programa\033[m")
            try:
                opcao = 0
                opcao = int(input("\033[34mSua opção: \033[m"))
            except ValueError:
                pass
            except KeyboardInterrupt:
                print("")
            try:
                if opcao not in [1, 2, 3]:
                    print("\033[31mErro: Por favor, Digite uma opção válida!\033[m")
            except NameError:
                print("\033[31mErro: Por favor, Digite uma opção válida!\033[m")
            else:
                break

        return opcao

    def nome_do_filme(self) -> str:
        """Input que pergunta o título do filme e dá erro se estiver vazio

        Retorna:
            str: o título digitado pelo usuário
        """
        while True:
            try:
                filme = input("\033[33mTítulo do Filme: \033[m").strip().title()
            except KeyboardInterrupt:
                print("")
            try:
                if filme == "":
                    print("\033[31mErro: Por favor, Digite um filme válido!\033[m")
            except NameError:
                print("\033[31mErro: Por favor, Digite um produto válido!\033[m")
            else:
                break

        return filme

    def ano_do_filme(self) -> int:
        """Input que pergunta o ano de lançamento do filme e dá erro se não for um número inteiro

        Retorna:
            int: o ano digitado pelo usuário
        """
        while True:
            try:
                ano_filme = int(input("\033[33mAno de Lançamento: \033[m"))
            except ValueError:
                print("\033[31mErro: Por favor, Digite um ano válido!\033[m")
            else:
                break

        return ano_filme

    def deseja_continuar(self) -> str:
        """Input que pergunta se o usuário deseja continuar

        Retorna:
            str: a resposta do usuário
        """
        resposta = " "
        while resposta not in "sn" or resposta == "" or resposta == "sn":
            try:
                resposta = (
                    input("\033[33mDeseja Continuar? [S/N]: \033[m").strip().lower()
                )
                if resposta not in "sn" or resposta == "" or resposta == "sn":
                    print("\033[31mErro: Por favor, Digite somente S ou N!\033[m")
            except KeyboardInterrupt:
                print("")
                print("\033[31mErro: Por favor, Digite somente S ou N!\033[m")
        if resposta == "n":
            return resposta


class Lista:
    """Essa classe é relacionada a listas"""

    def __init__(self, lista: list):
        self.lista = lista

    def ver_lista(self):
        """Essa função "printa" a lista de filmes"""
        print("\033[35mLista de Filmes:\033[m")
        sleep(1)

        for filme in range(0, len(self.lista), 2):
            titulo = self.lista[filme]
            ano = self.lista[filme + 1]

            print(f"\033[34m{titulo} ({ano})\033[m")
            sleep(1)

    def adicionar_dados(self, titulo: str, ano: int):
        """adiciona o título e o ano do filme para a lista

        Argumentos:
            titulo (str): o título do filme
            ano (int): o ano de lançamento do filme
        """
        self.lista.append(titulo)
        self.lista.append(ano)


# Criando objetos para o programa

lista_de_filmes = []

arquivo = Arquivo()
input_de_dados = Input_de_Dados()

# Programa Principal

while True:

    lista_de_filmes = arquivo.carregar_lista()
    lista = Lista(lista_de_filmes)

    print("\033[35mLocadora\033[m")
    sleep(1)

    opcao = input_de_dados.opcoes()

    if opcao == 1:
        while True:
            titulo = input_de_dados.nome_do_filme()
            ano = input_de_dados.ano_do_filme()

            lista.adicionar_dados(titulo, ano)
            arquivo.salvar_lista(lista.lista)

            resposta = input_de_dados.deseja_continuar()
            if resposta == "n":
                break

    if opcao == 2:
        lista.ver_lista()

    if opcao == 3:
        break

print("\033[31mFim do Programa\033[m")
sleep(1)
