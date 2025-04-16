# meu decorator (tem como importar ela como uma função normal!)
def marcador_inicio_fim_de_funcao(minhafuncao):
    def wrapper():
        print('A Função iniciou')
        minhafuncao()
        print('A Função terminou')

    return wrapper


@marcador_inicio_fim_de_funcao
# minha função
def ola_mundo():
    print('Olá, Mundo!')

ola_mundo()
