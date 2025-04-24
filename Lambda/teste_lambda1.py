from time import sleep

while True:
    try:
        preco = float(input('\033[36mPreço: \033[m'))
    except (ValueError, KeyboardInterrupt):
        print('\033[31mErro: Por Favor, Digite um preço válido!\033[m')
    else:
        break

calcular_imposto = lambda preco: preco * 0.3
# aqui está reclamando de usar lambda pois eu estou atribuindo ela a uma variável (calcular_imposto) então faria mais sentido usar def pois ele é mais legível e fácil de entender
# antes dos dois pontos você coloca os valores para a lambda funcionar
# geralmente a variável se chama x (ao invés de preco)

print(f'\033[35mO preço do imposto é de R${calcular_imposto(preco):.2f}\033[m')
sleep(1)
