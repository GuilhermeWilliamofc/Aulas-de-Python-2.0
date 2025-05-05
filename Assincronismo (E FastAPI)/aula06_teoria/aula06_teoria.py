import databases
from sqlalchemy import MetaData, Table, Column, Integer, String
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

# Criar a conexão
url_database = 'sqlite:///schema.db'
database = databases.Database(url_database)

# Descrever Tabelas
metadados = MetaData()
pessoa = Table('pessoas', metadados, Column('id', Integer, primary_key=True), Column('name', String))

# Fazer Query
async def obter_pessoas():
    query = pessoa.select()
    resultado = await database.fetch_all(query)
    return resultado

app = FastAPI()

@app.get('/')
async def ler_dados():
    await database.connect()
    people = await obter_pessoas()
    print(people)

    pessoas_formatadas = []
    for pessoa in people:
        pessoas_formatadas.append(pessoa['name'])

    await database.disconnect()
    return JSONResponse(content={'pessoas': pessoas_formatadas}, status_code=200)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
