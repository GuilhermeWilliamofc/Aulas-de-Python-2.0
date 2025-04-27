import asyncio
from googletrans import Translator

# peguei o def que criei para o pokémon e criei esse mini tradutor

async def tradutor(texto: str):
    async with Translator() as traduzir:
        resultado = await traduzir.translate(texto, dest='pt')
        print(f'\033[35m{resultado.origin} --> {resultado.text}\033[m')

texto = input('\033[33mDigite o Texto que quer traduzir: \033[m').strip()
asyncio.run(tradutor(texto))
