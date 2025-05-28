import asyncio
from src.model.settings.db_connection_handler import db_connection_handler
from src.model.repositories.pessoa_repository import PessoasRepository


async def rodar_pessoas():
    await db_connection_handler.connect_to_db()

    repo = PessoasRepository()
    pessoas = await repo.obter_pessoas()

    for pessoa in pessoas:
        print(pessoa.name)

    await db_connection_handler.disconnect_to_db()


asyncio.run(rodar_pessoas())
