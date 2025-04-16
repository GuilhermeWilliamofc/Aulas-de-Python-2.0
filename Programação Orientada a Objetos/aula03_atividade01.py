from time import sleep

# classe pessoa
class Pessoa:
    def __init__(self, nome, altura, idade): # a atividade não pediu nome mas eu quero colocar, além de mais algumas coisinhas
        self.nome = nome
        self.altura = altura
        self.idade = idade

    def correr(self):
        print(f'\033[33m{self.nome} está correndo...\033[m')
        sleep(2)
        print(f'\033[32m{self.nome} já está cansado de tanto correr!\033[m')

    def comer(self):
        print(f'\033[33m{self.nome} está comendo...\033[m')
        sleep(2)
        print(f'\033[32m{self.nome} já comeu!\033[m')

    def dados(self):
        print(f'Dados da Pessoa:\nNome: {self.nome}\nIdade: {self.idade} anos\nAltura: {self.altura:.2f}m')

# lista de termos proibidos de serem digitados no nome
proibidos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '/', '\\', '[', ']', '{', '}', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?', '~', '`', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# entrada de dados
while True:
    while True:
        nome = input('Nome: ').strip().capitalize()
        if nome == '' or nome.isnumeric() == True or any(caracteres in proibidos for caracteres in nome):
            print('\033[31mErro: Por favor, digite um nome válido!\033[m')
        else: 
            break

    while True:
        try:
            altura = float(input('Altura: '))
        except:
            print('\033[31mErro: Por favor, digite uma altura válida!\033[m')
        else:
            break

    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('\033[31mErro: Por favor, digite uma idade válida!\033[m')
        else:
            break

    # utilizando a classe pessoa
    pessoa = Pessoa(nome, altura, idade)
    pessoa.dados()
    pessoa.comer()
    pessoa.correr()

    # perguntar ao usuário se quer continuar
    resposta = ' '
    while resposta not in 'sn':
        try:
            resposta = input('\033[33mDeseja Continuar? [S/N]: \033[m').strip().lower()[0]
        except:
            pass
        if resposta not in 'sn':
            print('\033[31mErro: Por favor, digite sim ou não!\033[m')
    if resposta == 'n':
        break

print('\033[31mFim do Programa\033[m')
