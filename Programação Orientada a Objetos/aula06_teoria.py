# a teoria só tem a classe mas dei umas melhorias e realmente fiz o sistema cadastral só para treinar
# a teoria fala sobre SOLID (S) - Responsabilidade Única, onde devemos separar as responsabilidades do programa

class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validar_input(nome, idade):
            self.__registrar_usuario(nome, idade)
        else:
            self.__tratamento_de_erros()

    def __validar_input(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int) # 1
    
    def __registrar_usuario(self, nome: str, idade: int) -> None:
        print('\033[33mAcessando o banco de dados...\033[m') # 2
        print(f'\033[32mCadastrando usuário {nome}, idade: {idade} anos\033[m')

    def __tratamento_de_erros(self) -> None:
        print('\033[31mDados inválidos!\033[m') # 3


def input_cadastrar():
    """realiza o sistema cadastral, com input de nome e idade e acessa o banco de dados
    """
    nome = ler_nome()
    idade = ler_idade()

    cadastro = SistemaCadastral()
    cadastro.cadastrar(nome, idade)


def ler_nome():
    """lê o nome e apresenta erro se tiver números ou o nome tiver vazio

    Returns:
        str: nome
    """
    while True:
        try:
            nome = input('Nome: ').capitalize().strip()
            if not nome.isdigit() and not nome.isspace() and nome.isalpha():
                break
            else:
                erro('Nome', False)            
        except:
            print('')
            erro('Nome', False)

    return nome


def ler_idade():
    """lê a idade e apresenta erro se não for um inteiro

    Returns:
        int: idade
    """
    while True:
        try:
            idade = int(input('Idade: '))
        except KeyboardInterrupt:
            print('')
            erro('Idade', True)
        except:
            erro('Idade', True)
        else:
            break
    return idade

def erro(tipo, genero = False):
    """mostra uma mensagem de erro de acordo com o nome do input que deu erro

    Args:
        tipo (str): o nome do erro (ex: Nome, Idade -> 'Digite uma Idade Válida!')
        genero (bool, optional): o gênero do tipo, Falso é Masculino e True é Feminino. Falso por padrão.
    """
    if genero:
        genero_1 = 'uma'
        genero_2 = 'a'
    else:
        genero_1 = 'um'
        genero_2 = 'o'
    print(f'\033[31mErro: Por Favor, Digite {genero_1} {tipo} Válid{genero_2}!\033[m')


input_cadastrar()
