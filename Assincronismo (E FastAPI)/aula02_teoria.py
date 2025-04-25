# puramente teoria esse arquivo, sem código rodando...

# I/O -> Troca de informações entre sistemas

# exemplos:
# I/O -> Busca em banco de dados
# I/O -> Chamada a API externa

# I/O -> Geralmente é a troca de um sistema com seu terceiro

# exe
# chamar_uma_api() I/O -> Bloqueante
# chamar_outra_api() I/O -> Bloqueante

# exe
# chamar_uma_api() chamar_outra_api() I/O -> Não Bloqueante

# async def minha_func():
#   await(
#         chamar_um_banco(),
#         chamar_outra_api()
#)

# ou

# async def minha_func():
#   await chamar_um_banco()
#   await chamar_outra_api()

# async - indica que uma função deve ser executada de forma assíncrona
# await - indica que o "input" será paralisado naquele ponto aguardando um resultado futuro, ou seja, o controle de execução será dado à outro "input" e só será retomado quando o resultado ficar pronto
# na linha acima o termo certo não é input (só coloquei para facilitar), na verdade o termo certo é corrotina (outro nome para "async def" pelo oq entendi)
