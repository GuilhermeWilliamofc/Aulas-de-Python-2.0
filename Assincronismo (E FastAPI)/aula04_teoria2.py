import asyncio
import httpx
from googletrans import Translator

# modifiquei o script anterior para o usuário poder digitar o nome do pokémon que ele quer ver os dados

async def chamada_api(cliente: any, nome: str):
    url = f'https://pokeapi.co/api/v2/pokemon/{nome}' # a url da API do pokémon
    resposta = await cliente.get(url) # await aqui pois vai esperar a resposta
    data = resposta.json()

    nome = str(data['name']) # uma "filtragem" dos dados que a API enviou
    habilidade_original = str(data['moves'][0]['move']['name'])
    tipo_original = str(data['types'][0]['type']['name'])

    habilidade = await tradutor(habilidade_original) # tava dando dor de cabeça usar essa função nova de traduzir q nem ensinou no vídeo mas tava dando erro pq esqueci do await
    tipo = await tradutor(tipo_original)

    print(f'\033[34mDados do Pokémon ({nome.capitalize()}):\033[m') # print com os dados filtrados
    print(f'\033[35mNome:\033[33m {nome.capitalize()}\n\033[32mTipo: \033[33m{tipo.capitalize()}\n\033[36mHabilidade: \033[33m{habilidade.capitalize()}\033[m')


async def tradutor(texto: str): # o vídeo não ensinou esse def, eu criei por conta própria lendo a documentação
    async with Translator() as traduzir:
        resultado = await traduzir.translate(texto, dest='pt')
        return resultado.text


async def main(nome_pokemon: str):
    async with httpx.AsyncClient() as cliente: # aparentemente o httpx é tipo um requests mas é para requisições assincronas, o "as" dá o apelido do código para cliente
        await chamada_api(cliente, nome_pokemon) # usa o def que criamos anteriormente utilizando o cliente, nessa linha é uma requisição sincrona

while True:
    nome_pokemon = input('\033[33mDigite o Nome do Pokémon: \033[m').strip().lower()
    try:
        asyncio.run(main(nome_pokemon))
    except Exception as erro:
        print(f'\033[31mErro ({erro}): Por favor, Digite o nome de um Pokémon válido!\033[m')
    else:
        resposta = ' '
        while resposta not in 'sn' or resposta == '':
            resposta = input('\033[35mDeseja Continuar? [S/N]: \033[m').strip().lower()
            if resposta not in 'sn' or resposta == '':
                print('\033[31mErro: Por favor, responda somente com S ou N!\033[m')
        if resposta == 'n':
            break

print('\033[33mFim do Programa\033[m')
