from src.model.settings.db_connection_handler import db_connection_handler
from src.model.entities.pessoas import pessoa

class PessoasRepository:
    def __init__(self):
        self.__connection = db_connection_handler.get_connection()

    async def obter_pessoas(self):
        query = pessoa.select()
        resultado = await self.__connection.fetch_all(query)
        return resultado