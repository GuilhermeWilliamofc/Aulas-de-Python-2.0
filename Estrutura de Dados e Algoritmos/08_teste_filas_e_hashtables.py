from collections import defaultdict
from time import sleep

cidades_dict = defaultdict(list)

aeroporto_origem = ["São Paulo (Guarulhos - GRU)"]
capitais_brasil = [
    "Rio de Janeiro (Galeão - GIG)",
    "Brasília (Presidente Juscelino Kubitschek - BSB)",
    "Belo Horizonte (Confins - CNF)",
    "Recife (Guararapes - REC)",
    "Salvador (Deputado Luís Eduardo Magalhães - SSA)",
    "Curitiba (Afonso Pena - CWB)",
    "Porto Alegre (Salgado Filho - POA)",
    "Fortaleza (Pinto Martins - FOR)",
    "Manaus (Eduardo Gomes - MAO)",
    "Florianópolis (Hercílio Luz - FLN)",
    "Belém (Val-de-Cans - BEL)",
    "Vitória (Eurico de Aguiar Salles - VIX)",
    "Natal (Aluízio Alves - NAT)",
    "João Pessoa (Presidente Castro Pinto - JPA)",
    "Maceió (Zumbi dos Palmares - MCZ)",
    "São Luís (Marechal Cunha Machado - SLZ)",
    "Teresina (Senador Petrônio Portella - THE)",
    "Campo Grande (Internacional de Campo Grande - CGR)",
    "Cuiabá (Marechal Rondon - CGB)",
]
cidades_dict["Brasil"] += capitais_brasil

lista_passageiros = [
    "Ana",
    "João",
    "Mariana",
    "Carlos",
    "Fernanda",
    "Bruno",
    "Luana",
    "Gabriel",
    "Juliana",
    "Thiago",
    "Paula",
    "Rafael",
    "Camila",
    "Lucas",
    "Patrícia",
    "Felipe",
    "Débora",
    "Matheus",
    "Sofia",
    "Diego",
]

número_do_voo = [
    "GRU1023",
    "GIG2087",
    "BSB9001",
    "LAT4510",
    "AZU3205",
    "TAM8762",
    "GOL1178",
    "VAR9900",
    "ONE7634",
    "VOE2340",
    "WEB5555",
    "AVA6701",
    "KLM2453",
    "AFR3398",
    "JAL4480",
    "BAW1296",
    "IBE3417",
    "AAL5120",
    "UAL1093",
    "EMI7784",
]

status_voo = [
    "Aguardando",
    "Embarque iniciado",
    "Embarque encerrado",
    "Pronto para decolar",
    "Decolou",
    "Em voo",
    "Aterrissou",
    "Atrasado",
    "Cancelado",
    "Reprogramado",
]


class Pilha:
    def __init__(self):
        self.itens = []

    def adicionar(self, valor) -> None:
        self.itens.append(valor)

    def tamanho(self) -> int:
        return len(self.itens)

    def remover(self):
        if self.tamanho != 0:
            return self.itens.pop()

    def printar(self):
        print(self.itens)


class Fila:
    def __init__(self):
        self.entrada_de_dados = Pilha()
        self.saida_de_dados = Pilha()

    def __iter__(self):  # serve para a estrutura for in
        return iter(self.entrada_de_dados.itens + self.saida_de_dados.itens[::-1])

    def tamanho(self):
        return self.entrada_de_dados.tamanho() + self.saida_de_dados.tamanho()

    def adicionar_na_fila(self, item):
        self.entrada_de_dados.adicionar(item)

    def remover_da_fila(self):
        if not self.saida_de_dados.itens:
            while self.entrada_de_dados.itens:
                self.saida_de_dados.adicionar(self.entrada_de_dados.remover())
        return self.saida_de_dados.remover()

    def printar_fila(self):
        if len(self.entrada_de_dados.itens) != 0:
            print(self.entrada_de_dados.itens[::-1])
        else:
            self.saida_de_dados.printar()


class Printar:
    def titulo(self) -> None:
        print("\033[34mBem-Vindo ao Aeroporto Internacional de Guarulhos\033[m")
        sleep(1)

    def opcoes(self) -> int:
        print("\033[32mSistema de Gerenciamento de Voos Internacionais\033[m")
        print("\033[34m[ 1 ] - Chamar próximo voo")
        print("[ 2 ] - Exibir fila de passageiros aguardando voo")
        print("[ 3 ] - Adicionar passageiro à fila de espera")
        print("[ 4 ] - Sair do programa\033[m")
        while True:
            try:
                opcao = int(input("\033[33mSua Opção: "))
            except ValueError:
                print("\033[31mErro: Por Favor, Digite uma opção válida!")
            except KeyboardInterrupt:
                print("")
                print("\033[31mErro: Por Favor, Digite uma opção válida!")
            else:
                return opcao

    def voo_origem(self, passageiro) -> None:
        from random import choice, randint

        cidade = list(cidades_dict.values())  # choice só funciona com lista

        cidade_escolhida = choice(choice(cidade))
        número_escolhido = choice(número_do_voo)
        status_escolhido = choice(status_voo)
        print(f"\033[33m{passageiro} entrou no Voo:")
        print(f"Voo {número_escolhido}")
        print(f"Origem: {aeroporto_origem[0]}")
        print(f"Destino: {cidade_escolhida}")
        print(f"Horário de Decolagem: {randint(11, 19)}:{randint(10, 59)}")
        print(f"Status: {status_escolhido}\033[m")
        sleep(3)

    def voo_destino(self, passageiro):
        from random import choice, randint

        cidade = list(cidades_dict.values())
        cidade_escolhida = choice(choice(cidade))
        número_escolhido = choice(número_do_voo)
        status_escolhido = choice(status_voo)
        print(f"\033[33m{passageiro} entrou no Voo:")
        print(f"Voo {número_escolhido}")
        print(f"Origem: {cidade_escolhida}")
        print(f"Destino: {aeroporto_origem[0]}")
        print(f"Horário de Decolagem: {randint(11, 19)}:{randint(10, 59)}")
        print(f"Status: {status_escolhido}\033[m")
        sleep(3)

    def lista_de_passageiros(self):
        cont = 1
        print("\033[35mFila de Passageiros aguardando voo:")
        if passageiros.tamanho() != 0:
            for pessoa in passageiros:  # __iter__ sendo utilizado
                print(f"{cont}º - {pessoa}")
                cont += 1
                sleep(0.5)
        else:
            print("\033[31mNão há mais passageiros aguardando voo\033[m")


passageiros = Fila()
for passageiro in lista_passageiros:
    passageiros.adicionar_na_fila(passageiro)

# printar titulo
# printar voo e seus dados e remover da lista
# lista de pessoas pegando voo

printar = Printar()
printar.titulo()

while True:
    opcao = 0
    while opcao not in [1, 2, 3, 4]:
        opcao = printar.opcoes()
        if opcao not in [1, 2, 3, 4]:
            print("\033[31mErro: Por Favor, Digite uma opção válida!")

    if opcao == 1:
        from random import choice

        try:
            pessoa = passageiros.remover_da_fila()
            comandos = choice([printar.voo_origem, printar.voo_destino])
            comandos(pessoa)
        except IndexError:
            print("\033[31mErro: Não há mais passageiros aguardando voo\033[m")

    if opcao == 2:
        printar.lista_de_passageiros()

    if opcao == 3:
        novo_passageiro = ""
        while novo_passageiro == "":
            novo_passageiro = (
                input(
                    "\033[33mDigite o Nome do Passageiro (Digite '.' para voltar): \033[m"
                )
                .strip()
                .title()
            )
            if novo_passageiro == "":
                print("\033[31mErro: Por Favor, Digite um nome válido!")
        if novo_passageiro != ".":
            passageiros.adicionar_na_fila(novo_passageiro)

    if opcao == 4:
        break

print("\033[31mFim do Programa\033[m")
