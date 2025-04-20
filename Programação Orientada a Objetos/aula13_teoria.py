from time import sleep
# a teoria é sobre injeção de dependência novamente, onde uma classe depende da outra para funcionar

class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.conectar = False
    
    def conectar_ao_banco(self) -> None:
        print('\033[33mConectando ao Banco de Dados...\033[m')
        sleep(1)
        self.conectar = True
        print('\033[32mConectado com sucesso!\033[m')

class RepositorioDeBanco:
    def __init__(self, conexao: ConectorBancoDeDados):
        self.__conexao = conexao

    def busca_dados(self) -> list:
        try:
            lista = [1, 2, 3, 4, 5]
            print('\033[33mBuscando Dados...\033[m')
            sleep(1)
            if self.__conexao.conectar:
                print('\033[32mDados Encontrados com sucesso!\033[m')
                return lista
            else:
                print('\033[31mErro durante a procura dos dados, verifique sua conexão e tente novamente\033[m')
        except (TypeError, AttributeError):
            print('\033[31mErro durante a procura dos dados, verifique sua conexão e tente novamente\033[m')

class RegraDeNegocio:
    def __init__(self, repositorio: RepositorioDeBanco):
        self.__repositorio = repositorio

    def calcular_resultados(self):
        try:
            resultado = 0
            dados = self.__repositorio.busca_dados()
            print('\033[33mCalculando Resultados...\033[m')
            sleep(1)
            if self.__repositorio.busca_dados:
                for dado in dados:
                    resultado += dado
                print(f'\033[32mO Resultado do cálculo dos dados é igual a {resultado}\033[m')
            else:
                print('\033[31mErro durante o cálculo dos dados, verifique sua conexão e tente novamente\033[m')
        except (TypeError, AttributeError):
            print('\033[31mErro durante o cálculo dos dados, verifique sua conexão e tente novamente\033[m')

banco = ConectorBancoDeDados()
banco.conectar_ao_banco()

repositorio = RepositorioDeBanco(banco)

regra = RegraDeNegocio(repositorio)
regra.calcular_resultados()
