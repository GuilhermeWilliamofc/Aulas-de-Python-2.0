import asyncio
import httpx
from googletrans import Translator

# a teoria é sobre Assincronismo na Prática, utilizando API dessa vez

async def chamada_api(cliente: any, nome: str):
    url = f'https://pokeapi.co/api/v2/pokemon/{nome}' # a url da API do pokémon
    resposta = await cliente.get(url) # await aqui pois vai esperar a resposta
    data = resposta.json()

    nome = str(data['name']) # uma "filtragem" dos dados que a API enviou
    habilidade_original = str(data['moves'][0]['move']['name'])
    tipo_original = str(data['types'][0]['type']['name'])

    habilidade = await tradutor(habilidade_original) # tava dando dor de cabeça usar essa função nova de traduzir q nem ensinou no vídeo mas tava dando erro pq esqueci do await
    tipo = await tradutor(tipo_original) # dá para usar asyncio.create_task()...

    print(f'\033[34mDados do Pokémon ({nome.capitalize()}):\033[m') # print com os dados filtrados
    print(f'\033[35mNome:\033[33m {nome.capitalize()}\n\033[32mTipo: \033[33m{tipo.capitalize()}\n\033[36mHabilidade: \033[33m{habilidade.capitalize()}\033[m')
    print()


async def tradutor(texto: str): # o vídeo não ensinou esse def, eu criei por conta própria lendo a documentação
    async with Translator() as traduzir:
        resultado = await traduzir.translate(texto, dest='pt')
        return resultado.text


async def main():
    async with httpx.AsyncClient() as cliente: # aparentemente o httpx é tipo um requests mas é para requisições assincronas, o "as" dá o apelido do código para cliente
        await chamada_api(cliente, 'pikachu') # usa o def que criamos anteriormente utilizando o cliente, nessa linha é uma requisição sincrona
        await asyncio.gather(chamada_api(cliente, 'charizard'), chamada_api(cliente, 'mew'), chamada_api(cliente, 'ditto')) # usando o gather para uma requisição assincrona
        print('\033[34mFim\033[m')

asyncio.run(main()) # usando o run() para explicar qual def quero rodar de forma assincrona, só funciona fora de um async def
