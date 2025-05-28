from fastapi import FastAPI
from vendas import *

app = FastAPI()


@app.get("/")  # semelhante ao route do flask
def home():
    return {"Total de Vendas": total_vendas}


@app.get("/vendas/{idvenda}")  # colocar entre chaves é semelhante as variaveis do flask
def pegar_venda(idvenda: int):  # precisa declarar o tipo da variavel
    if idvenda in vendas:
        return mostrar_venda(idvenda)
    else:
        return f'Erro! O Id "{idvenda}" Não foi encontrado no banco de dados!'
