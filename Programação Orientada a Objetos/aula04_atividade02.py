class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

    def mostrar_dados(self):
        print(f'Nome: {self.nome}\nCPF: {self.__cpf}')

    def get_cpf(self):
        print(f'{self.__cpf}')

    def set_cpf(self, novo_cpf):
        if novo_cpf.isdigit() and len(novo_cpf) == 11:
            self.__cpf = novo_cpf
            print(f'\033[32mCPF alterado com sucesso!\033[m')
        else:
            print(f'\033[31mCPF inválido!\033[m')

pessoa = Pessoa('Guilherme', '12345678900')
pessoa.mostrar_dados()
pessoa.get_cpf()

pessoa.set_cpf('00123456789')
pessoa.mostrar_dados()
