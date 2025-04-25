from time import sleep

precos = []

while True:
    try:
        preco = float(input('\033[36mPreço: \033[m'))
    except (ValueError, KeyboardInterrupt):
        print('\033[31mErro: Por Favor, Digite um preço válido!\033[m')
    else:
        precos.append(preco)
        resposta = ' '
        while resposta not in 'sn' or resposta == '':
            resposta = input('\033[33mDeseja Continuar? [S/N]: \033[m').strip().lower()
            if resposta not in 'sn' or resposta == '':
                print('\033[31mErro: Por Favor, Responda somente com S ou N!\033[m')
        if resposta == 'n':
            precos = list(set(precos)) # tirar valores repetidos
            precos.sort() # organizar em ordem crescente por precaução já que o set embaralha a ordem
            break

impostos = list(map(lambda x: x * 0.3, precos)) # um dos casos onde lambda é útil, pois elimina a necessidade de um def
# uma dica para aprender lambda é fazer com def primeiro e depois tentar adaptar para lambda

# "Em vez de usar um loop for , a função map() fornece uma maneira de aplicar uma função a todos os itens em um iterável. Portanto, muitas vezes ela pode ser mais eficiente"
# "A função map() em Python é usada para aplicar uma função a cada item de um iterável (como uma lista, tupla, etc.) e retornar um novo iterável com os resultados. É uma forma eficiente e concisa de transformar elementos de um iterável sem precisar de loops explícitos."
# agora o list no map() é para "dizer" que quero que "retorne" como uma lista

print('-' * 37)
titulo_imposto = '\033[32mPreço dos Impostos\033[m'
print(f'{titulo_imposto:^45}')
print('-' * 37)
sleep(1)

for preco, imposto in zip(precos, impostos): 
    # "A função zip() é usada para juntar duas ou mais listas em uma única lista de tuplas, onde cada tupla contém um elemento de cada uma das listas fornecidas. A função zip() é muito útil quando precisamos percorrer duas ou mais listas simultaneamente, pois elimina a necessidade de usar loops aninhados."
    print(f'\033[35mO preço do imposto de R${preco:.2f} é R${imposto:.2f}\033[m')
    sleep(1)
